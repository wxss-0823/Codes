#include <iostream>
#include <Windows.h>


BYTE BACKUP[5];
void Unhook(void* src, int len) {
	DWORD old;
	VirtualProtect(MessageBoxW, len, PAGE_EXECUTE_READWRITE, &old);
	memcpy(MessageBoxW, BACKUP, len);
	VirtualProtect(MessageBoxW, len, old, &old);
}

void Hook32(void* src, void* tar, int len) {
	DWORD old;
	VirtualProtect(src, len, PAGE_EXECUTE_READWRITE, &old);
	memcpy(BACKUP, src, len);
	*(BYTE*)src = 0xE9;
	// x64 need 8 byte addr, 1 byte opt code
	uintptr_t relativeAddress = (uintptr_t)tar - (uintptr_t)src - 5;
	// disassembly need occupied the rest 5 byte otp code
	*(DWORD*)((BYTE*)src + 1) = relativeAddress;
	//*(WORD*)((BYTE*)src + 5) = 0x9090;
	//*(BYTE*)((BYTE*)src + 13) = 0x90;
	VirtualProtect(src, len, old, &old);
}

int WINAPI MyMsgBoxW(
	_In_opt_ HWND hWnd,
	_In_opt_ LPCWSTR lpText,
	_In_opt_ LPCWSTR lpCaption,
	_In_ UINT uType)
{
	lpText = L"Hook";
	Unhook(MessageBoxW, 5);
	MessageBoxW(hWnd, lpText, lpCaption, uType);
	Hook32(MessageBoxW, MyMsgBoxW, 5);
	return 0;
}


int main() {
	//MyMsgBoxW(0, L"Hook", 0, 0);
	Hook32(MessageBoxW, MyMsgBoxW, 5);
	MessageBoxW(0, L"Hello", 0, 0);
	MessageBoxW(0, L"Hello", 0, 0);
	MessageBoxW(0, L"Hello", 0, 0);
	return 0;
}