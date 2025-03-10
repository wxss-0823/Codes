#include <iostream>
#include <Windows.h>

int nScreenWidth = 120;
int nScreenHeight = 40;

int main() 
{
	// Create Screen Buffer
	wchar_t* screen = new wchar_t[nScreenHeight * nScreenWidth];
	HANDLE hConsole = CreateConsoleScreenBuffer(GENERIC_READ | GENERIC_WRITE, 0, NULL, CONSOLE_TEXTMODE_BUFFER, NULL);
	SetConsoleActiveScreenBuffer(hConsole);
	DWORD dwBytesWritten = 0;

	screen[nScreenWidth * nScreenHeight - 1] = '\0';
	WriteConsoleOutputCharacterW(hConsole, screen, nScreenWidth * nScreenHeight, { 0,0 }, &dwBytesWritten);

	return 0;
}