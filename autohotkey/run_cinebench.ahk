MsgBox, Please select the directory containing "Cinebench.exe"
FileSelectFolder, PATH
PATH := RegExReplace(PATH, "\\$")  ; Removes the trailing backslash, if present.

runwait, %ComSpec% " /c (%PATH%\Cinebench.exe g_CinebenchMinimumTestDuration=1 g_CinebenchAllTests=true) >> %PATH%\log.txt"
; runwait, %ComSpec% " /c (%PATH%\Cinebench.exe g_CinebenchMinimumTestDuration=1 g_CinebenchCpuXTest=true) >> %PATH%\log.txt"
; runwait, %ComSpec% " /c (%PATH%\Cinebench.exe g_CinebenchMinimumTestDuration=1 g_CinebenchCpu1Test=true) >> %PATH%\log.txt"

FileRead, CINEBENCH_OUTPUT, %PATH%\log.txt

; ahk uses PCRE regex
RegExMatch(CINEBENCH_OUTPUT, "(Processor\s*\:\s)\K\d*", CORE_COUNT)
RegExMatch(CINEBENCH_OUTPUT, "s)Single.*CB\s\K\d*\.\d*", SINGLE_CORE_SCORE)
RegExMatch(CINEBENCH_OUTPUT, "s)CB\s\K\d*\.\d*(?=.*Single)", MULTI_CORE_SCORE)

ESTIMATED_SINGLE_CORE_SCORE := round(MULTI_CORE_SCORE / CORE_COUNT, 2)

OUTPUT =
(
Cinebench R23 Multi core Score: %MULTI_CORE_SCORE%
Cinebench R23 Single core Score: %SINGLE_CORE_SCORE%
Number of Cores in This Machine: %CORE_COUNT%
Cinebench R23 Estimated Single Core: %ESTIMATED_SINGLE_CORE_SCORE%
)

FileDelete, %PATH%\output.txt
FileAppend, %OUTPUT%, %PATH%\output.txt

MsgBox, A file has been generated at "%PATH%\output.txt"
