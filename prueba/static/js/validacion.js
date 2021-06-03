
    const nombre  = document.getElementById("full_name")
    const form  = document.getElementById("form-group row")

    form.addEventListener("submit", e=>{
        e.preventDefault()
        let warnings = ""
        if(nombre.value.length < 6){
            warnings += `El nombre o no es valido <br>`
        }
    })