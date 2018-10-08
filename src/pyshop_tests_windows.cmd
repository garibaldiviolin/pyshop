@echo off & setLocal EnableDELAYedeXpansion

rem Verify django tests
coverage run --source ./ ./manage.py test manager restapi website > coverage_result.txt 2>&1
findstr "OK" coverage_result.txt > nul
if not %ERRORLEVEL% == 0 (
    echo "PyShop tests failed."
    goto :eof
) else (
    echo "PyShop tests OK!"
)

rem Verify coverage tests
coverage report > coverage_report.txt
findstr "TOTAL" coverage_report.txt > coverage_result.txt
findstr "100%" coverage_result.txt > nul
if not %ERRORLEVEL% == 0 (
    echo "Coverage tests failed."
    goto :eof
) else (
    echo "Coverage tests OK!"
)

rem Remove coverage logs
del coverage_result.txt
del .coverage

rem Verify code with pylint_runner (uses pylint)
pylint_runner > pylint_result.txt
findstr "at 10.00/10" pylint_result.txt > nul
if not %ERRORLEVEL% == 0 (
    echo "pylint_runner tests failed. See pylint_result.txt for details."
    goto :eof
) else (
    echo "pylint_runner tests OK!"
)
