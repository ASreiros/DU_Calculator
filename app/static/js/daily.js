function daily_allowance_check(){
    console.log("Lets check daily allowance");
    daily = document.querySelector("#country").value
    days = document.querySelector("#numberofdays").value

    data={
        daily:daily,
        days:days,
    }
    
    if(daily != "-1"){
        fetch(`${window.origin}/countallowance`,{
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
                document.querySelector('#daily').value = data["daily"]
                document.querySelector('#suma').value = data["allowance"]
            })

        })
    } 
}



document.querySelector("#numberofdays").addEventListener("input", (e)=>{
    days = Math.round(Number(e.target.value))
    if (days < 1){
        days = "1"        
    } 
    document.querySelector("#numberofdays").value = days
    daily_allowance_check()
})
document.querySelector("#country").addEventListener("change", ()=>{
    daily_allowance_check()
})
