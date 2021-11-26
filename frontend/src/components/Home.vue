<template>
    <div class="container">
        <h1>¡Estos amigos esperan por tí!</h1>  
               
        <div v-for="pet in allPets.slice(0,12)"  v-bind:key="pet.pet_id" class="target">
            <img :src="pet.pet_image"/>
            <div class="nombre"><p>{{pet.pet_name}}</p></div>
            <div class="info"><p><b>Edad:  </b>{{pet.pet_age}}</p></div>
            <div class="info"><p><b>Tamaño:  </b>{{pet.pet_size}}</p></div>
            <div class="info"><p><b>Personalidad:  </b>{{pet.pet_description}}</p></div>
            <button class="btn-adoptar" v-on:Click="loadSolicitud(pet.pet_id)">Adoptar</button>
        </div>
    </div>
</template>

<script> 
    import axios from 'axios'

    export default {
        name: 'Home',  

        data: function(){
            return {                
                allPets:"",                               
            }
        },

        methods:{
            getAllPets: async function(){
                await axios.get('https://backend-compatitas.herokuapp.com/pet/all', {headers: {}})
                .then((result) => {                                  
                let auxAllPets=result.data.data;                
                this.randomPet(auxAllPets)                
                })
                .catch(() => {
                
                });
            },

            randomPet: function(data){
                let auxAllPets=data                
                let auxDict=[];
                while(auxAllPets.length>0){                    
                    var num = Math.floor((Math.random() * (auxAllPets.length)))                     
                    auxDict.push(auxAllPets[num])                                      
                    auxAllPets.splice(num,1)                    
                }

                let auxList=[]
                for (var i=0;i<auxDict.length;i++){                    
                    if (auxDict[i].pet_status!="adoptado"){                                               
                        auxList.push(auxDict[i])                        
                    }
                }    
                console.log('Pets loaded')            
                this.allPets=auxList;
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

    ul{
        display:flex;
    }

    .container{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-around;
        margin: auto;
        width: 80%;
        padding-bottom: 100px ;   
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;         
    }
    
    h1{
        width: 100%;
        color: #9D84B7;
        text-align: center;
    }

    .target{
        display: flex;
        width: 20%;
        height: 430px;
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
        margin: 5px;
        padding: 8px;
        bottom: 15px;
        position: relative;
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

    .btn-adoptar button:hover {
        color: #B2F9FC;
        font-weight: 600;
    }

</style>