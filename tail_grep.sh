#!/usr/bin/env bash
# на случай если такого файла
# не существовало
# или в нём что-то уже было,
# запишем в него пустоту
:> /tmp/t.txt
# tail -f => "follow" новые строки
#                     в файле
# grep -i python => искать вхождение
#                   подстроки python
tail -f /tmp/t.txt | grep -i python
