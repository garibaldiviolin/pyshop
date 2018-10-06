# verify tests coverage
coverage run --source ./ ./manage.py test manager restapi website &> /dev/null
result=`coverage report | tail -c 5`

if [ $result != "100%" ]; then
    coverage report
    echo "Coverage tests failed."
    exit 1
else
    echo "Coverage tests OK!"
fi

# verify code with pylint_runner (uses pylint)
pylint_runner > pylint_result.txt
result=`head -n-1 pylint_result.txt | tail -n 1`
if [[ ! $result =~ "at 10.00/10" ]]; then
    echo $result
    echo "pylint_runner tests failed. See pylint_result.txt for details."
    exit 2
else
    echo "pylint_runner tests OK!"
fi

