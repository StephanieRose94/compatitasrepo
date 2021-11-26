<template>

    <div>
        <div class="container_formulario_adop">
            <h1>Formulario de adopcion</h1>
            <div class="colum1">
            <div  class="tarjeta_formulario">
                
            <img :src="pet.pet_image"/>
                <div class="nombre"><p>{{pet.pet_name}}</p></div>
                <div class="info"><p><b>Edad:  </b>{{pet.pet_age}}</p></div>
                <div class="info"><p><b>Tamaño:  </b>{{pet.pet_size}}</p></div>
                <div class="info"><p><b>Personalidad:  </b>{{pet.pet_description}}</p></div>
            
        
            </div> 
            </div>
            <form action="" method="get" id="contact">
            <div class="colum2">
                <label for="nombre"><b>Nombre</b></label>
                <p class="info_formulario">{{request.applicant_name}}</p>
                <label for="documento"><b>N° Documento</b></label>
                <p class="info_formulario">{{request.document_id}}</p>
                </div>
                <div class="colum3">
                
                <label for="apellido" ><b>Apellido</b></label>
                <p class="info_formulario">{{request.applicant_last_name}}</p>
                <label for="edad"><b>Edad</b></label>
                <p class="info_formulario">{{request.applicant_age}}</p>
                </div>
                <div class="colum4">
                <label for="direccion"><b>Direccion completa</b></label>
                <p class="info_formulario">{{request.address}}</p>
                </div>
                <div class="colum5">
                <label for="telefono"><b>Teléfono</b></label>
                <p class="info_formulario">{{request.phone}}</p>
                <label for="email"><b>E-mail</b></label>
                <p class="info_formulario">{{request.email}}</p>
                </div>
                <div class="colum6">
                <label for="ingresos"><b>Ingresos</b></label>
                <p class="info_formulario">{{request.income}}</p>
                <label for="actividad"><b>economica</b></label>
                <p class="info_formulario">{{request.activity}}</p>
                </div>
                <div class="colum7">
                <label for="razon"><b>¿Por que desea adoptar?</b></label>
                <p class="info_formulario">{{request.reason}}</p>
                </div>
                
                <h2>{{verifyEnded(request.request_status)}}</h2>

                <select v-if="!labelEnded" v-on:Change="updateRequest" name="estado" class="estado_solicitud">
                    <option value="1" id="pendiente" :selected="verifyState('pendiente',request.request_status)">Pendiente</option> 
                    <option value="2" id="aceptada" :selected="verifyState('aceptada',request.request_status)">Aceptada</option> 
                    <option value="3" id="rechazada" :selected="verifyState('rechazada',request.request_status)">Rechazada</option>
                </select>

                </form>
            

            <button type="submit" class="volver_admin" id="volver_admin"><router-link to="/administrador">Volver a Solicitudes</router-link></button> 
            
        </div>
    </div>
</template>

<script> 
    import axios from 'axios'
    
    export default {
        name: 'Administrador_solicitudes',  

        data: function(){
            return {  
                labelEnded:"",
                allRequest:"",
                ended:"",
                request:"",              
                pet:"",     
                requestUpdate:{                    
                    activity: "",
                    address: "",
                    admin_id: "",
                    applicant_age: "",
                    applicant_last_name: "",
                    applicant_name: "",
                    document_id: "",
                    email: "",
                    income: "",
                    pet_id: "",
                    phone: "",
                    reason: "",
                    request_code: "",    
                    request_status: ""
                }           
                          
            }
        },

        methods:{
            
            getAllRequest: async function(){
                let id=localStorage.getItem('request')                
                await axios.get('https://backend-compatitas.herokuapp.com/request/all', {headers: {}})
                .then((result) => {                                  
                    this.allRequest=result.data.data; 
                })
                .catch(() => {
                    
                });
            },

            getRequest: async function(){
                let id=localStorage.getItem('request')                
                await axios.get(`https://backend-compatitas.herokuapp.com/request/${id}`, {headers: {}})
                .then((result) => {                                  
                    this.request=result.data;  
                    this.labelEnded=false;                   
                })
                .catch(() => {
                    
                });
            },

            getPet: async function(){    
                let id=localStorage.getItem('pet')
                await axios.get(`https://backend-compatitas.herokuapp.com/pet/${id}`, {headers: {}})
                .then((result) => {   
                this.pet=result.data                 
                })
                .catch(() => {
                    alert('Error');
                });                
            },

            updateRequest: async function(){                
                if (document.getElementById('aceptada').selected){
                    this.request.request_status="aceptada" 
                    this.pet.pet_status="adoptado"
                }else if (document.getElementById('rechazada').selected){
                    this.request.request_status="rechazada" 
                    this.pet.pet_status="disponible"               
                }else{
                    this.request.request_status="pendiente" 
                    this.pet.pet_status="disponible"               
                }               

                await axios.put(`https://backend-compatitas.herokuapp.com/request/update/${this.request.request_id}`, this.request,{headers: {}})
                .then((result) => {   
                    alert(result.data)                 
                })
                .catch(  (error) => {
                  console.log(error.response.data)
                });

                await axios.put(`https://backend-compatitas.herokuapp.com/pet/update/${this.pet.pet_id}`, this.pet,{headers: {}})
                .then((result) => {   
                    //alert(result.data)                 
                })
                .catch(  (error) => {
                  console.log(error.response.data)
                });                
                
                await this.getAllRequest()

                for (var i=0;i<this.allRequest.length;i++){

                    let id=this.allRequest[i].pet_id
                    if (this.allRequest[i].request_id!=this.request.request_id){
                        if(this.allRequest[i].pet_id==this.pet.pet_id){                            
                            let requestId=this.allRequest[i].request_id  
                            let auxRequest="";                         
                            await axios.get(`https://backend-compatitas.herokuapp.com/request/${requestId}`, {headers: {}})
                                .then((result) => {                                  
                                    auxRequest=result.data; 
                                    auxRequest.request_status="finalizada" 
                                })
                                .catch(() => {
                                    
                                });
                            
                            await axios.put(`https://backend-compatitas.herokuapp.com/request/update/${auxRequest.request_id}`, auxRequest,{headers: {}})
                                .then((result) => {   
                                    //alert(result.data)                 
                                })
                                .catch(  (error) => {
                                console.log(error.response.data)
                                });
                            
                        }
                        
                    }
                     
                }
                

            },

            verifyState: function(sender,state){
                if (sender==state){
                return true
                }else{
                return false
                }
            },

            verifyEnded: function(status){
                //console.log(status)
                if (this.request.request_status=="finalizada"){
                    this.labelEnded=true
                    return "finalizada"
                }
            }      
            
        },
        
        mounted:function(){
            this.getRequest();
        },

        created: async function(){
            this.getPet();
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
    padding: 2px;
    color: #606060;
}
.info_formulario{
    width: 80%;
    padding: 3px;
    border: solid 0.5px rgb(212, 212, 212);
    border-radius: 2px;
    display: flex;
    flex-direction: initial;
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
width: 100%;
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
width: 100%;
height: 80px;
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

.estado_solicitud{
  
  border: none;
  width: 20%;
  background-color: #091353;
     font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: white;
    font-size: 16px;
    margin: 5px;
    padding: 10px;
    border-radius: 3px;
}

.volver_admin{


cursor: pointer;    
        background-color:#9D84B7;
        width: 30%;
        padding: 8px;
        margin-top: 100px;
        margin-bottom: 50px;
        bottom: 15px;
   border-radius: 5px;
   border-style: none;
    
   
}
.volver_admin a{
text-decoration: none;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 20px;
        font-weight: 700;
}

</style>