<template>
    <div>
        <div class="container">
            <h1>Quiero Adoptar</h1>
            <p>Selecciona una o varias de las siguientes opciones</p>
            <form action="" class="formularioBusqueda">
                <div class="formularioAdop">
                <label for="Tipo" >
                <h4> Tipo de mascota</h4>
                    <p><input type="radio" name="tipo" id="gato">Gato</p> 
                    <p><input type="radio" name="tipo" id="perro">Perro </p>
                </label></div>
                <div class="formularioAdop">
                <label for="Edad">
                <h4> Edad </h4>
                    <p><input type="radio" name="edad" id="cachorro">Cachorro</p> 
                    <p><input type="radio" name="edad" id="adulto">Adulto </p>
                </label></div>
                <div class="formularioAdop">
                <label for="Tamano">
                    <h4>Tamaño</h4>
                    <p><input type="radio" name="tamano" id="pequeño">Pequeño</p>
                    <p><input type="radio" name="tamano" id="mediano">Mediano</p>
                    <p><input type="radio" name="tamano" id="grande">Grande</p>
                </label></div>                
                
            </form>
            <div class="botonbuscar">
                <button v-on:Click="selectPet" type="submit" class="buscarMascota" id="buscarMascota"><b>Buscar</b></button> 
                </div>                


            <div v-for="pet in somePets"  v-bind:key="pet.pet_id" class="target">
                <img :src="pet.pet_image"/>
                <div class="nombre"><p>{{pet.pet_name}}</p></div>
                <div class="info"><p><b>Edad:  </b>{{pet.pet_age}}</p></div>
                <div class="info"><p><b>Tamaño:  </b>{{pet.pet_size}}</p></div>
                <div class="info"><p><b>Personalidad:  </b>{{pet.pet_description}}</p></div>
                <button class="btn-adoptar" v-on:Click="loadSolicitud(pet.pet_id)">Adoptar</button>
            </div>
        </div>
    </div>
</template>

<script> 
import axios from 'axios'

    export default{
        name: 'Adopcion',    

    data: function(){
            return {                
                allPets:"",   
                somePets:"",                            
            }
        },

        methods:{
            getAllPets: async function(){
                await axios.get('https://backend-compatitas.herokuapp.com/pet/all', {headers: {}})
                .then((result) => {    
                let auxPets=result.data.data
                let auxList=[]
                for (var i=0;i<auxPets.length;i++){                    
                    if (auxPets[i].pet_status!="adoptado"){                                               
                        auxList.push(auxPets[i])                        
                    }
                }                               
                this.allPets=auxList;  
                this.somePets=auxList; 
                this.selectPet();                
                })
                .catch(() => {
                
                });
            },  
            
            selectPet: async function(){
                this.selectPetType()
                this.selectPetAge()
                this.selectPetSize()
            },

            selectPetType: async function(){                
                let type="" 
                this.somePets=[]
                if (document.getElementById('perro').checked){
                    type="perro"
                }
                else if (document.getElementById('gato').checked){
                    type="gato"
                }else{
                    this.somePets=this.allPets;
                    return                    
                }
                for(var i=0;i<this.allPets.length;i++){
                    if (this.allPets[i].pet_type==type){
                        this.somePets.push(this.allPets[i])
                    }
                }           
            },
            
            selectPetAge: async function(){                
                let age="";   
                let auxPets=[];             
                if (document.getElementById('cachorro').checked){
                    age="cachorro"
                }
                else if (document.getElementById('adulto').checked){
                    age="adulto"
                }else{                       
                    return                 
                }
                for(var i=0;i<this.somePets.length;i++){
                    if (this.somePets[i].pet_age==age){
                        auxPets.push(this.somePets[i])
                    }
                }        
                this.somePets=auxPets                        
            },

            selectPetSize: async function(){                
                let size="";   
                let auxPets=[];             
                if (document.getElementById('pequeño').checked){
                    size="pequeño"
                }
                else if (document.getElementById('mediano').checked){
                    size="mediano"
                }
                else if (document.getElementById('grande').checked){                       
                    size="grande"                
                }else{
                    return
                }
                for(var i=0;i<this.somePets.length;i++){
                    if (this.somePets[i].pet_size==size){
                        auxPets.push(this.somePets[i])
                    }
                }        
                this.somePets=auxPets                        
            },

            loadSolicitud: function(id){                
                localStorage.setItem('pet',id)
                this.$emit('loadSolicitud')
            },
        },
        
        created: async function(){
            this.getAllPets();
        }
    }
</script>



<style>

  .formularioAdop label{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
   
}

  .formularioAdop p{
    width: 100%;
    display: flex;
    flex-direction: row;
    
}

.formularioAdop input{
    display: inline-block;
position: relative;
top: 5px;
border: 2px solid #ccc;
width: 18px;
height: 18px;
background: #fff;
}


.formularioBusqueda{
    width: 100%;
 display: flex;
    justify-content: space-around;
    margin: auto;
}
.buscarMascota{
  
cursor: pointer;    
        background-color:#9D84B7;
        width: 50%;
        padding: 8px;
        margin:auto;
        bottom: 15px;
   border-radius: 5px;
   border-style: none;
    
   
}

.buscarMascota b {
text-decoration: none;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 20px;
        font-weight: 700;
}
.botonbuscar{
   
    width: 80%;
    margin: auto;
    margin-top: 10px;
    margin-bottom: 10px;

}





.container{
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: space-around;
    margin: auto;
    width: 80%;
    padding-bottom: 100px ;
    text-align: center;
    
}
h1{
    width: 100%;
    color: #9D84B7;
}
.target{
    display: flex;
    width: 20%;
    height: 430px;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    flex-direction: column;
    -webkit-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
-moz-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
position: relative;


}
.target img{
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

    .btn-adoptar{
    
        background-color:#B2F9FC;
        color: #091353;
        width: 90%;
        margin: auto;
        padding: 8px;
        bottom: 15px;
   position: absolute;
   border-radius: 5px;
   border-style: none;

        
    }

    .btn-adoptar a{
        text-decoration: none;
        color: #091353;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: 500;
    }


</style>