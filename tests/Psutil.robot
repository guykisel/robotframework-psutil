*** Settings ***
Force Tags        psutil
Test Timeout      1 minute
Library           PsutilLibrary

*** Test Cases ***
Can Get User Name
    ${users}=    PsutilLibrary.Users
    Should Not Be Empty    ${users[0].name}

Can Get Process IDs
    ${pids}=    PsutilLibrary.Pids
    Should Not Be Empty    ${pids}

*** Keywords ***
