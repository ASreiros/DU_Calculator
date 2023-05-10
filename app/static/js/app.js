console.log("Hello from app.js");
last_change = "amount-brutto"

function zero_values(){
    document.getElementById("amount-netto").value = '0'
    document.getElementById("amount-brutto").value = '0'
    document.getElementById("amount-netto-hour").value = '0'
    document.getElementById("amount-brutto-hour").value = '0'
    document.getElementById("hours").value = '1'
}

function collect(id){
    netto = parseFloat(document.getElementById("amount-netto").value);
    brutto = parseFloat(document.getElementById("amount-brutto").value);
    nettoHour = parseFloat(document.getElementById("amount-netto-hour").value);
    bruttoHour = parseFloat(document.getElementById("amount-brutto-hour").value);
    hour = parseFloat(document.getElementById("hours").value);
    if(isNaN(netto)||isNaN(brutto)||isNaN(nettoHour)||isNaN(bruttoHour)|| isNaN(hour) || brutto< 0 || netto < 0 || bruttoHour < 0 || nettoHour < 0 || hour < 1){
        netto = 0
        brutto = 0
        nettoHour = 0
        bruttoHour = 0
        zero_values()
    }
    

    data = {
        id:id,
        netto:netto,
        brutto:brutto,
        bruttoHour:bruttoHour,
        nettoHour:nettoHour,
        hour:hour,     
    }

    document.querySelectorAll(".setting-box").forEach(box=>{
        setting = box.id
        data[setting] = document.querySelector(`#${setting}>.active`).dataset.value
    })

    
    if(netto>0 || brutto > 0 || nettoHour > 0 || bruttoHour > 0){
        fetch(`${window.origin}/calculate`,{
            method: "POST",
            credentials: "include",
            body:JSON.stringify(data),
            cache:"no-cache",
            headers: new Headers({
                "content-type":"application/json"
            })
        })
        .then(function(response){
            if (response.status != 200){
                console.log("Response status is not 200:  ", response.status, response.statusText);
                return
            }

            response.json().then(function(info){
                data = info[0]['data']
                document.querySelectorAll('.salary-input-holder>input').forEach(input=>{
                    if(input.id != id && input.id != "hours"){
                        document.getElementById(input.id).value = data[input.id]; 
                    }
                })
                taxes = data["taxes"]
                taxesList = Object.keys(taxes)
                taxesList.forEach(tax=>{
                    document.querySelector(`#tax-${tax} p`).innerHTML = data["taxes"][tax]
                })
                if (Number(data['amount-brutto']) > 0){
                    document.querySelector('#pdf-button').style.display = "block"
                } else{
                    document.querySelector('#pdf-button').style.display = "none"
                }
            })


        })
    } 

}

elements = document.querySelectorAll('.salary-input-holder>input')
elements.forEach(element => {
    element.addEventListener('input', function(){
        if(element.id != "hours"){
            last_change = element.id
        }
        collect(last_change)     
    });   
});


buttons = document.querySelectorAll('.choice')
buttons.forEach(btn => {
    btn.addEventListener('click', ()=>{
        if (!btn.classList.contains('active')){
            parentId = btn.parentElement.id;
            siblings = document.querySelectorAll(`#${parentId} .choice`)
            siblings.forEach(el=>{
                el.classList.remove('active')
            })
            btn.classList.add("active");
            collect(last_change)
            }
    })    
})


settings = document.querySelectorAll('.setting-btn-container')
settings.forEach(btn => {
    btn.addEventListener('click', ()=>{
        id = btn.id
        tumblers = document.querySelectorAll(`#${id}>.div-btn>*`)
        tumblers.forEach(tumbler => {
            tumbler.classList.toggle('active')
        })
        if (id == "s-set"){
            document.querySelectorAll(".temp").forEach(box => {
                box.classList.toggle('noshow')
            });
        } else{
            document.querySelector('#s-hour').classList.toggle('noshow')
        }    
    })
})

document.querySelector('#pdf-button').addEventListener("click", function(){

const aElement = document.createElement('a');
aElement.setAttribute('download', 'pdf');
const href = "/getpdf"
aElement.href = href;
aElement.setAttribute('target', '_blank');
aElement.click();
aElement.remove();
});

