/* Validacion de formularios*/
(function (){
  'use strict'
  var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function(form){
      form.addEventListener('submit', function(event){
        if (!form.checkValidity()){
          event.preventDefault()
          event.stopPropagation
        }
        form.classList.add('was-validated')
      }, false)
    })
})

/* Validacionde correo
document.getElementById('basic-addon1').addEventListener('input', function() {
    campo = event.target;
    valido = document.getElementById('emailOK');
        
  var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

 var regOficial = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

    //Se muestra un texto a modo de ejemplo, luego va a ser un icono
    if (reg.test(campo.value) && regOficial.test(campo.value)) {
      valido.innerText = "";
    } else if (reg.test(campo.value)) {
      valido.innerText = "";

    } else {
      valido.innerText = "Ingrese un correo valido";

}
});*/
/* Alerta pagina de inicio*/
function eventoInicio() {
  alert('ya te encuentra en la pagina de inicio')
}

/* API MASCOTAS*/
const API_URL = 'https://dog.ceo/api/breeds/list/all';

function mascota(){
  alert ('');
}

/* API CLIMA*/
window.addEventListener('load',()=>{
  let lat
  let lon

  let temperaturaValor = document.getElementById('temperatura_valor')
  let temperaturaDesc = document.getElementById('temperatura_desc')

  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition( posicion =>{

      lat = posicion.coords.latitude
      lon = posicion.coords.longitude

      const url = 'https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&lang=es&units=metric&appid=bc950522156b629d78634344eb37c406'
      
      fetch(url)
        .then(response => {return response.json()})
        .then( data => {
          console.log(data.weather[0].description)
          let temp= Math.round(data.main.temp)
          temperaturaValor.textContent= temp
          /*let desc = data.weather[0].description
          temperaturaDesc.textContent= desc*/

          console.log(data.weather[0].main)
          switch (data.weather[0].main) {
              case 'Thunderstorm':
                iconoAnimado.src='animated/thunder.svg'
                console.log('TORMENTA');
                break;
              case 'Drizzle':
                iconoAnimado.src='animated/rainy-2.svg'
                console.log('LLOVIZNA');
                break;
              case 'Rain':
                iconoAnimado.src='animated/rainy-7.svg'
                console.log('LLUVIA');
                break;
              case 'Snow':
                iconoAnimado.src='animated/snowy-6.svg'
                  console.log('NIEVE');
                break;                        
              case 'Clear':
                  iconoAnimado.src='animated/day.svg'
                  console.log('LIMPIO');
                break;
              case 'Atmosphere':
                iconoAnimado.src='animated/weather.svg'
                  console.log('ATMOSFERA');
                  break;  
              case 'Clouds':
                  iconoAnimado.src='animated/cloudy-day-1.svg'
                  console.log('NUBES');
                  break;  
              default:
                iconoAnimado.src='animated/cloudy-day-1.svg'
                console.log('por defecto');
            }
        })
        .catch(error => {
          console.log(error)
        })
    })
  }
});
