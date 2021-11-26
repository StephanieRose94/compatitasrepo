<template>
<div class="container">
    
<div class="estado">
        <form >            
               <label class="info" for="name">Código de solicitud:</label>
               <input type="text" v-model="request.code">
               <button v-on:Click="verifyCode(request.code)" class="btn-validar">Validar</button>
        </form>
        
   
    </div>

        <div v-if="aceptada" class="target_estado">
            <h2 class="aceptada">Tu solicitud ha sido aceptada</h2>
            <p class="info">Nos alegra confirmarte que desde ahora <b>"{{this.mascota.pet_name}}"</b> formará parte de tu familia. Pronto nos comunicaremos contigo para ultimar detalles sobre la entrega de tu nuevo amigo. </p>
            <p class="info">¡¡Mil gracias por tu ayuda!!</p>
        </div> <!-- Div para el caso en que la solicitud sea afirmativa-->


        <div v-if="rechazada" class="target_estado">
            <h2 class="denegada">Tu solicitud no ha sido denegada</h2>
            <p class="info">
                Lamentamos informar que tu solicitud de adopción ha sido denegada. Para más información comunícate con nosotros. 
            
                </p>

        </div> <!-- Div para el caso en que la solicitud sea negativa -->
        
        <div v-if="pendiente" class="target_estado">
            <h2 class="enproceso">Tu solicitud continua en proceso de validación</h2>
            <p class="info">
                No desesperes, tu solicitud está siendo evaluada por nuestros expertos. 
            </p>
        </div> <!-- Div para el caso en que la solicitud sea en proceso -->

        <div v-if="finalizada" class="target_estado">
            <h2 class="finalizada">Tu solicitud ha sido finalizada</h2>
            <p class="info">
                La mascota que elegiste fue adoptada por otra persona. Te invitamos a buscar otra mascota disponible. 
            </p>
        </div> <!-- Div para el caso en que la solicitud sea en proceso -->

        <button v-on:Click="loadHome" class="btn-volver">Volver al inicio</button>
</div>
</template>

<script>
import axios from 'axios'

    export default {

        name: 'Estado_solicitud',

        data: function(){
            return{
                aceptada:false,
                pendiente:false,
                rechazada:false,
                finalizada:false,
                mascota:"",
                request:{
                    code:""                    
                }
            }
        },

        methods:{
              
            verifyCode: async function(code){  
                await axios.get('https://backend-compatitas.herokuapp.com/request/all', {headers: {}})
                .then((result) => {                                                      
                    let auxAllRequest=result.data.data; 
                    this.aceptada=false;
                    this.pendiente=false;
                    this.rechazada=false;
                    this.finalizada=false;

                    for (var i=0;i<auxAllRequest.length;i++){  
                        
                        if (code==auxAllRequest[i].request_code){
                            if (auxAllRequest[i].request_status=="aceptada"){                                
                                this.aceptada=true
                                this.pendiente=false    
                                this.rechazada=false
                                this.finalizada=false
                                this.getPet(auxAllRequest[i].pet_id)
                            }
                            if (auxAllRequest[i].request_status=="rechazada"){                                
                                this.aceptada=false
                                this.pendiente=false    
                                this.rechazada=true
                                this.finalizada=false
                            }
                            if (auxAllRequest[i].request_status=="pendiente"){                                
                                this.aceptada=false
                                this.pendiente=true   
                                this.rechazada=false
                                this.finalizada=false
                            }
                            if (auxAllRequest[i].request_status=="finalizada"){                                
                                this.aceptada=false
                                this.pendiente=false   
                                this.rechazada=false
                                this.finalizada=true
                            }
                        }
                    } 
                    if (this.aceptada==false && this.pendiente==false && this.rechazada==false && this.finalizada==false) {
                    
                        alert('El código ingresado no existe')                        
                    }              
                })
                .catch(() => {
                    console.log(error.response.data)
                });
            },

            getPet: async function(petId){    
                let id=petId
                await axios.get(`https://backend-compatitas.herokuapp.com/pet/${id}`, {headers: {}})
                .then((result) => {   
                this.mascota=result.data                     
                })
                .catch(() => {
                    alert('Error');
                });                
            },

            loadHome: function(){                
                this.$emit('loadHome')
            }
        },
        
    }
    
</script>

<style>

.estado{
    width: 100%;
    margin-bottom: 50px;    
}

.estado form{
    display: flex;
    flex-direction: row;

}
.estado label{
    width: 20%;
    margin-top: 15px;
    font-size: 20px;
}

.estado input{
    width: 60%;
    margin: 10px;
}
.estado button{
    width: 20%;
    margin: 10px;    
}

 .target_estado{
        display: flex;
        width: 80%;
        height: 100%;
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

    .target_estado p{
        padding: 10px;
    }
    .target_estado h2{
        margin-bottom: 30px;
    }
    .aceptada{
        color: lawngreen;
    }
    .denegada{
        color: red;
    }
    .finalizada{
        color: rgb(206, 32, 119);
    }


 .btn-volver{
    
        background-color:#091353;
        color: white;
        width: 30%;
        margin: 30px;
        padding: 8px;
        bottom: 15px;
        position: relative;
        border-radius: 5px;
        border-style: none;        
    }

    .btn-volver a{
        text-decoration: none;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: 500;
    }


.btn-validar{
    
        background-color:#9D84B7;
        color: white;

        padding: 8px;

        position: relative;
        border-radius: 5px;
        border-style: none;        
    }

    .btn-validar a{
        text-decoration: none;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: 500;
    }

</style>