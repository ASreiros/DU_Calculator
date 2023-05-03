console.log("Hello from app.js");



function collect(){
    netto = parseFloat(document.getElementById("amount-netto").value);
    brutto = parseFloat(document.getElementById("amount-brutto").value);
    total = parseFloat(document.getElementById("amount-total").value);
    if(isNaN(netto)||isNaN(brutto)){
        netto = 0
        brutto = 0
    }
    console.log(netto, brutto, total);
}

elements = []
netto = document.getElementById("amount-netto");
brutto = document.getElementById("amount-brutto");
elements.push(netto, brutto);

elements.forEach(element => {
    element.addEventListener('input', function(){
        collect()
    });   
});


buttons = document.querySelectorAll('.choice')
buttons.forEach(btn => {
    btn.addEventListener('click', ()=>{
        if (!btn.classList.contains('active')){
            parentId = btn.parentElement.id;
            console.log(parentId);
            siblings = document.querySelectorAll(`#${parentId} .choice`)
            siblings.forEach(el=>{
                el.classList.remove('active')
            })
            btn.classList.add("active");
            collect()
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



