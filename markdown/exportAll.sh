for d in *
do
    if [ "$d" == *"template"* ] || [ "$d" == *"integrations"* ] || [ "$d" == *"exportAll.sh"* ]
    then
        continue
    fi
    cd "$d" && ./export.sh
    cd -
done
