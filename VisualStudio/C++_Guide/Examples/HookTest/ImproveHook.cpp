#include <iostream>
#include <Windows.h>


using PFN = int (WINAPI*) (
	_In_opt_ HWND hWnd,
	_In_opt_ LPCWSTR lpText,
	_In_opt_ LPCWSTR lpCaption,
	_In_ UINT uType);

PFN pfn = nullptr;

void ImpHook32(void* src, void* tar, int len) {
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
}

void* Trampoline(void* src, void* tar, int len) {
	BYTE* gateway = (BYTE*)VirtualAlloc(0, len + 5, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy(gateway, src, len);
	*(gateway + len) = 0xe9;
	*(DWORD*)(gateway + len + 1) = (BYTE*)src - gateway - 5;
	ImpHook32(src, tar, len);
	return gateway;
}

int WINAPI ImpMyMsgBoxW(
	_In_opt_ HWND hWnd,
	_In_opt_ LPCWSTR lpText,
	_In_opt_ LPCWSTR lpCaption,
	_In_ UINT uType)
{
	lpText = L"Hook";
	pfn(hWnd, lpText, lpCaption, uType);
	return 0;
}


int ImpMain() {
	//MyMsgBoxW(0, L"Hook", 0, 0);
	pfn = (PFN)Trampoline(MessageBoxW, ImpMyMsgBoxW, 5);
	MessageBoxW(0, L"Hello", 0, 0);
	MessageBoxW(0, L"Hello", 0, 0);
	MessageBoxW(0, L"Hello", 0, 0);
	pfn(0, L"Hello", 0, 0);
	return 0;
}