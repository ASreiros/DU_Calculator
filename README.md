# DU_Calculator
This is salary calculator according to Lithuanian law 2023
It can calculate salary befote taxes, given the after taxes amount and vice versa.
Additional functionality in the top right link allows to find daily allowance in business trips according to Lithuanian Law.

## Link to working demo
This project is hosted: https://salary-asreiros.koyeb.app/

## Main page functionality:
* located at https://salary-asreiros.koyeb.app/ homepage
* (before taxes -> brutto, cash payment after taxes -> netto)
* Calculation brutto salary to netto salary
* Calculation netto salary to brutto salary
* Calculation hourly brutto payment to netto, brutto, hourly netto
* Calculation hourly netto payment to netto, brutto, hourly brutto
* Calculation can be downloaded as PDF. Download button is availible when amount of brutto payment is more then 0.
* Calculation accepts NPD setting(should it be used or not)
* Calculation accepts SODRA "floor" setting(according to Lithuanian law employer sometimes have to pay taxes from minimum salary, even if salary is bellow minimum. This setting tells should we consider this)
* Calculation accepts setting if employee is recieving a pension(it is important for GPM tax)
* Calculation accepts setting if employee is a Lithuanina citizen(it is important for PSD tax)
* Calculation accepts setting if work agreement is term or nonterm(important for employer taxes)
* Calculation accepts setting which incedent category employer has(important for employer taxes)

## Dienpinigiai functionality:
* located at https://salary-asreiros.koyeb.app/dienpinigiai
* Accepts country (From dropdown list)
* Accepts number of days(int, days > 0)
* Gives daily allowance amount per day and  total amount of daily allowance according to Lithuanian law

## Technology used
* Python (Flask) for backend
* HTML, CSS, Javascript for front end.
* All calculations, even simplest ones are done at backend, frontend responsible only for the visual part  
* Full project requirements can be seen at requirement.txt


## Start
* flask run

## Contact
* Anton Sokolkin 
* email: ansokolkin@gmail.com
* github: https://github.com/ASreiros


