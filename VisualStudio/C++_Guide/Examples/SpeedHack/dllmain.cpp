// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <Windows.h>
#pragma comment(lib,"winmm.lib")

using PfnTimeGetTime = DWORD(WINAPI*)();
using PfnGetTickCount = DWORD(WINAPI*)();
using PfnQueryPerformanceCounter = BOOL(WINAPI*)(LARGE_INTEGER*);

PfnTimeGetTime pfnTimeGetTime = nullptr;
PfnGetTickCount pfnGetTickCount = nullptr;
PfnQueryPerformanceCounter pfnQueryPerformanceCounter = nullptr;

DWORD startTime, startTickCount;
DWORD64 startPerformanceCount;

constexpr int factor = 3;

BOOL Hook32(void* src, void* tar, int len) {
	DWORD old;
	VirtualProtect(src, len, PAGE_EXECUTE_READWRITE, &old);
	*(BYTE*)src = 0xE9;
	// x64 need 8 byte addr, 1 byte opt code
	uintptr_t relativeAddress = (uintptr_t)tar - (uintptr_t)src - 5;
	// disassembly need occupied the rest 5 byte otp code
	*(DWORD*)((BYTE*)src + 1) = relativeAddress;
	//*(WORD*)((BYTE*)src + 5) = 0x9090;
	//*(BYTE*)((BYTE*)src + 13) = 0x90;
	VirtualProtect(src, len, old, &old);
	return true;
}

void* Trampoline(void* src, void* tar, int len) {
	BYTE* gateway = (BYTE*)VirtualAlloc(0, len + 5, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy(gateway, src, len);
	*(gateway + len) = 0xe9;
	*(DWORD*)(gateway + len + 1) = (BYTE*)src - gateway - 5;
	Hook32(src, tar, len);
	return gateway;
}

DWORD WINAPI myTimeGetTime() {
	DWORD current = pfnTimeGetTime();
	return current + (current - startTime) * factor;
}

DWORD WINAPI myGetTickTime() {
	DWORD current = pfnGetTickCount();
	return current + (current - startTickCount) * factor;
}

BOOL WINAPI myQueryPerformanceCounter(LARGE_INTEGER* out) {
	DWORD64 current;
	if (!pfnQueryPerformanceCounter((LARGE_INTEGER*)&current))
		return false;
	DWORD64 r = current + (current - startPerformanceCount) * factor;
	*out = *(LARGE_INTEGER*)&r;
	return true;
}

void InitializeStartTime() {
	QueryPerformanceCounter((LARGE_INTEGER*)&startPerformanceCount);
	startTickCount = GetTickCount();
	startTime = timeGetTime();
}

DWORD WINAPI MainThread(LPVOID param) {
	InitializeStartTime();

	auto hMod = GetModuleHandleA("kernel32.dll");
	pfnTimeGetTime = (PfnTimeGetTime)GetProcAddress(hMod, "timeGetTime");
	pfnGetTickCount = (PfnGetTickCount)GetProcAddress(hMod, "GetTickCount");
	pfnQueryPerformanceCounter = (PfnQueryPerformanceCounter)GetProcAddress(hMod, "QueryPerformanceCounter");

	pfnTimeGetTime = (PfnTimeGetTime)Trampoline(pfnTimeGetTime, myTimeGetTime, 9);
	pfnGetTickCount = (PfnGetTickCount)Trampoline(pfnGetTickCount, myGetTickTime, 7);
	pfnQueryPerformanceCounter = (PfnQueryPerformanceCounter)Trampoline(pfnQueryPerformanceCounter, myQueryPerformanceCounter, 5);

	return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		DisableThreadLibraryCalls(hModule);
		CloseHandle(CreateThread(0, 0, MainThread, 0, 0, 0));
	case DLL_THREAD_ATTACH:
	case DLL_THREAD_DETACH:
	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}

