# OpenFunds convert fieldlist



```bash
curl https://www.openfunds.org/fields/fieldlist.htm  > fieldlist.htm
```

The file fieldlist.htm is very big and contains a lot of redundant information.

Lets fix that
```bash
pandoc -s fieldlist.htm -t gfm-raw_html -o fieldlist.initial.md
```
