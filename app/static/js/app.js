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
        console.log(isNaN(netto), isNaN(brutto));
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
        // add:document.querySelector(`#s-add>.active`).dataset.value,
        // npd:document.querySelector(`#s-npd>.active`).dataset.value,
        // floor:document.querySelector(`#s-floor>.active`).dataset.value,     
    }

    document.querySelectorAll(".setting-box").forEach(box=>{
        setting = box.id
        data[setting] = document.querySelector(`#${setting}>.active`).dataset.value
    })
    console.log(data);

    
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
                console.log(info);
                data = info[0]['data']
                if(id == "amount-netto"){
                    document.getElementById("amount-brutto").value = data['brutto'];
                } else if((id == "amount-brutto")){
                    user_change_flag = false
                    document.getElementById("amount-netto").value = data['netto'];
                    user_change_flag = true 
                } else{
                    console.log("something went wrong. Probably wrong id");
                }
                taxes = data["taxes"]
                taxesList = Object.keys(taxes)
                taxesList.forEach(tax=>{
                    document.querySelector(`#tax-${tax} p`).innerHTML = data["taxes"][tax]
                })
            })


        })
    } 

}

elements = document.querySelectorAll('.salary-input-holder>input')
elements.forEach(element => {
    element.addEventListener('input', function(){
        collect(element.id)
        last_change = element.id
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



