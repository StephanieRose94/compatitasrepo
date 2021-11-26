<template>
    <div class="container_formulario_adop">
        <h1>Formulario de adopcion</h1>
        <div class="colum1">
            <div class="tarjeta_formulario">                
                <img :src="this.pet.pet_image"/>
                <div class="nombre"><p>{{this.pet.pet_name}}</p></div>
                <div class="info"><p><b>Edad:  </b>{{this.pet.pet_age}}</p></div>
                <div class="info"><p><b>Tamaño:  </b>{{this.pet.pet_size}}</p></div>
                <div class="info"><p><b>Personalidad:  </b>{{this.pet.pet_description}}</p></div>  
            </div> 
        </div>

        <form id="contact">
            <div class="colum2">
                <label for="nombre">Nombre</label>
                <input type="text" v-model="newRequest.applicant_name">
                <label for="documento">N° Documento</label>
                <input type="text" v-model="newRequest.document_id">
            </div>
                
            <div class="colum3">                
                <label for="apellido" >Apellido</label>
                <input type="text" v-model="newRequest.applicant_last_name">
                <label for="edad">Edad</label>
                <input type="text" v-model="newRequest.applicant_age">
            </div>

            <div class="colum4">
                <label for="direccion">Direccion completa</label>
                <input type="text" v-model="newRequest.address">
            </div>

            <div class="colum5">
                <label for="telefono">Teléfono</label>
                <input type="text" v-model="newRequest.phone">
                <label for="email">E-mail</label>
                <input type="email" v-model="newRequest.email">
            </div>

            <div class="colum6">
                <label for="ingresos">Ingresos</label>
                <input type="text" v-model="newRequest.income">
                <label for="actividad">Actividad economica</label>
                <input type="text" v-model="newRequest.activity">
            </div>
            
            <div class="colum7">
                <label for="razon">¿Por que desea adoptar?</label>
                <textarea v-model="newRequest.reason"></textarea>
            </div>
                
                <button v-if='!requestCreated' v-on:Click="completeRequest" class="enviar_solicitud" id="enviar_solicitud">Enviar solicitud</button> 
        </form>
            <h2 v-if='requestCreated' >Gracias por tu solicitud</h2>
            <p v-if='requestCreated' >Puedes consultar el estado de tu solicitud usando el codigo <b>{{this.code}}</b> en la sección <b> Estado solicitudes</b></p>
            <button v-if='requestCreated' class="enviar_solicitud backHome" ><router-link to="/home">Volver a Home</router-link></button> 
       
    </div>

</template>

<script> 
import axios from 'axios'

    export default {
        name: 'Formulario_adopcion',  

        data: function(){
            return{
                charSet:['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                requestCreated:false,
                pet:"",
                code:"",
                newRequest:{                    
	                applicant_name:"",
	                applicant_last_name:"",
	                document_id:"",
	                applicant_age:"",
	                address:"",
	                phone:"",
	                email:"",
	                income:"",
	                activity:"",
	                reason:"",
	                request_status:"pendiente",
	                pet_id:"",
	                admin_id:"1"
                }
            }
        },

        methods:{
            
            getPet: async function(){    
                let id=localStorage.getItem('pet')
                await axios.get(`https://backend-compatitas.herokuapp.com/pet/${id}`, {headers: {}})
                .then((result) => {   
                this.pet=result.data  
                this.requestCreated=false 
                console.log('Pet cathed')   
                })
                .catch(() => {
                    alert('Error');
                });                
            },

            completeRequest: function(){
                this.newRequest.pet_id=this.pet.pet_id                
                this.newRequest.request_code= this.generateCode() 
                this.sendRequest()
            },

            sendRequest: async function(){                                 
                await axios.post('https://backend-compatitas.herokuapp.com/request', this.newRequest,{headers: {}})
                .then((result) => {   
                      this.requestCreated=true       
                      console.log("Request Uploaded")         
                })
                .catch(  (error) => {
                  console.log(error.response.data)
                  alert('Existe algún error con los datos ingresados. Verifique y vuelva a intentarlo')
                });          
            },

            generateCode: function(){
                let code=""
                for(var i=0;i<6;i++){
                    var index = Math.floor((Math.random() * (this.charSet.length)))
                    code+=this.charSet[index] 
                }   
                this.code=code             
                return code               
            },

            
        },
        
        created: async function(){
            this.getPet()            
        }
    }
</script>

<style>

h1{
    width: 100%;
    color: #9D84B7;
}

.container_formulario_adop{

    margin: auto;
    width: 80%;
    color: #606060;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  
    padding-bottom: 100px;

    
}

label{
    width: 80%;
    display: flex;
    align-items: flex-start;
    padding: 7px;
    color: #606060;
}
input{
    width: 80%;
    padding: 3px;
}
.colum1{
float: left;
width: 40%;


}
.colum2{
float: left;
width: 30%;
display: flex;
flex-direction: column;
}
.colum3{
float: left;
width: 30%;
display: flex;
flex-direction: column;
}
.colum4{
float: left;
width: 60%;
display: flex;
flex-direction: column;
}

.colum4 input{
width: 90%;
}
.colum5{
float: left;
width: 30%;
display: flex;
flex-direction: column;
}
.colum6{
float: left;
width: 30%;
display: flex;
flex-direction: column;
}
.colum7{
float: left;
width: 60%;
display: flex;
flex-direction: column;
}
.colum7 textarea{
width: 90%;
height: 80px;
}

.enviar_solicitud{
    cursor: pointer;    
    background-color:#9D84B7;
    width: 200px;
    padding: 8px;
    margin-top: 30px;
    margin-bottom: 50px;
    bottom: 15px;
    border-radius: 5px;
    border-style: none;  
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
}

.enviar_solicitud a{
text-decoration: none;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 20px;
        font-weight: 700;
}

.backHome{
    margin-left:40%;
}



.tarjeta_formulario{
    display: flex;
    width: 70%;
    height: 480px;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    flex-direction: column;
    align-items: center;
    -webkit-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
-moz-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
position: relative;


}
.tarjeta_formulario img{
    width: 100%
    
}

.nombre{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
    font-size: 25px;
    color: #9D84B7;
    margin-top: -10px;
    padding: 0;
    }

    .info{
        color: #606060;
        padding: 0;
        margin-top: -25px;
    }


</style>