<template>
  <div>     
      
      <div class="container_admin">  
        <h1>Buzón de solicitudes</h1>
        <table class="solicitudes">
          <tr>

            <th>Nombre Solicitante</th>
            <th>Edad solicitante</th>
            <th>Mascota</th>
            <th>Más información</th>
            <th>Estado</th>

          </tr>

          <tr v-for="solicitud in allRequest"  v-bind:key="solicitud.request_id">
            
            <td>{{solicitud.applicant_name + " " + solicitud.applicant_last_name}}</td>
            <td>{{solicitud.applicant_age}}</td>
            <td>{{this.getPetName(solicitud.pet_id)}}</td>
            <td v-on:Click="loadDetails(solicitud.request_id, solicitud.pet_id)" class="link">Ver más...</td>
            <td>
              {{solicitud.request_status}}
              <!--<select name="estado" >
                <option value="1" :selected="verifyState('pendiente',solicitud.request_status)" >Pendiente</option> 
                <option value="2" :selected="verifyState('aceptada',solicitud.request_status)" >Aceptada </option> 
                <option value="3" :selected="verifyState('rechazada',solicitud.request_status)" >Rechazada</option>
                <option value="3" :selected="verifyState('finalizada',solicitud.request_status)" >Finalizada</option>
              </select>-->
            </td>
          </tr>
        </table>
      </div> 
    </div>
</template>

<script>

import axios from 'axios'

export default {

    name: 'Administrador',

    data: function(){
      return{        
        allRequest:"",
        pets:""
      }
    },

      
    methods:{

      getAllRequest: async function(){
              await axios.get('https://backend-compatitas.herokuapp.com/request/all', {headers: {}})
              .then((result) => {                                  
                this.allRequest=result.data.data; 
                this.endState=false;
              })
              .catch(() => {
                
              });

              await this.getAllPets()
      },

      getAllPets: async function(){
              await axios.get('https://backend-compatitas.herokuapp.com/pet/all', {headers: {}})
              .then((result) => {                                  
                this.pets=result.data.data; 
              })
              .catch(() => {
                
              });
      },      

      loadDetails: function(id,pet_id){        
        localStorage.setItem('request',id)
        localStorage.setItem('pet',pet_id)        
        this.$router.push({name:"Administrador_solicitudes"})
      },

      getPetName: function(id){
        for (var i=0;i<this.pets.length;i++){
          if (id==this.pets[i].pet_id){            
            return this.pets[i].pet_name
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

    },
   

    created: async function(){

      this.getAllRequest();

    }

}

</script>

<style>
.container_admin{
    display: flex;
    flex-direction: column;
    margin: auto;
    width: 80%;
    padding-bottom: 100px ;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    
}

.logout{
cursor: pointer;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
font-size: 20px;
width: 80px;
padding: 10px;
margin-top: 20px;
margin-left: 20px;
display: flex;
flex-direction: row;
background-color: #091353 ;
border: none;
border-radius: 10px ;
-webkit-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
-moz-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
}

.logout a{
    text-decoration: none;
    color: white;
}

.logout a:hover {
  color: #B2F9FC;
  font-weight: 600;
}
table{
  border-spacing: 0;
}
th{
  border:solid 1px white;
  background-color: #9D84B7;
  color: white;
  margin: 0;
  padding: 10px;
}
td{
  border:solid 1px #9D84B7;
  margin: 0;
  padding: 5px;
}
td a{
  text-decoration: none;
  color:darkcyan;
}
select{
  
  border: none;
  width: 100%;
     font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    font-size: 16px;
}

.link {
  cursor: pointer;
  color:rgb(34, 175, 34);
}
</style>