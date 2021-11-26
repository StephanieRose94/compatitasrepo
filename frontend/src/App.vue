<template>
  <div class='main' id="main">

    <div class='header' id='header'>
      <img src="./assets/banner.jpg" alt="compatitas" srcset="">
      
        <button v-if="!isAuth" v-on:Click="loadLogin">Iniciar sesión</button>
        <button v-if="isAuth" v-on:Click="endSesion">Cerrar sesión</button>
      
    </div> 
    <div v-if="!isAuth" class="menu">
      <ul>        
        <li><router-link to="/home">Home</router-link></li>
        <li><router-link to="/adopcion">Amigos que esperan hogar</router-link></li>
        <li><router-link to="/mision">Misión</router-link></li>
        <li><router-link to="/donaciones">Donaciones</router-link></li>
        <li ><router-link to="/estado_solicitud">Estado solicitudes</router-link></li>
      </ul>
    </div>  
    
    <router-view 
      v-on:endSesion="endSesion"
      v-on:loadAdministrador="loadAdministrador"
      v-on:loadSolicitud="loadSolicitud"
      v-on:loadHome="loadHome"      
    >
    </router-view>  
    
    <div class="footer">
        <div class="container_footer">
          <div class="red">  
              <img src="./assets/facebook.png" alt="">              
              <h4>Facebook</h4>
          </div>
          <div class="red"> 
              <img src="./assets/instagram.png" alt="">
              <h4>Instagram</h4>                
          </div>
          <div class="red"> 
              <img src="./assets/twitter.png" alt="">
               <h4>Twitter</h4>
          </div>          
        </div>
        <p class="copy">Copyright © 2021 | MisionTic2022 </p>
    </div>
  </div>
</template>

<script>

export default {
  
  name: 'App',

  data: function(){
    return{
      isAuth: false,            
    }
  },

  components:{
  },

  methods:{

    verify: function(data){      
      this.isAuth= data.value              
    },

    loadLogin: function(){          
      this.$router.push({name:'Login'})
    },

    endSesion: function(){
      let a={value:false}     
      this.$router.push({name:'root'})    
      this.verify(a)
    },

    loadHome: function(){
      this.$router.push({name: 'Home'})
    },

    loadAdministrador: function(){
      let a={value:true}  
      this.$router.push({name: 'Administrador'})
      this.verify(a)
    },

    loadSolicitud: function(){       
      this.$router.push({name: 'Formulario_adopcion'})
    },

    completedLogin: function(){
      console.log("completedLogin")
    },



  }
  
}

</script>


<style>

  body{
    margin: 0;
    padding: 0;
    width: 100%;   
  }

  .header{
    width: 100%;
    display: flex;
    margin: 0;
    background-size: cover;
    position: relative;
    justify-content: flex-end;
  }

  .header button{
    /*display: block;*/
    cursor: pointer;
    position: absolute;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20px;
    margin: 20px;
    padding: 10px;
    background-color: #091353 ;
    border: none;
    border-radius: 10px ;
    -webkit-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
    -moz-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
    box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
    text-decoration: none;
    color: white;
  }

  .header button:hover {
    color: #B2F9FC;
    font-weight: 600;
  }

  
.footer{
  width: 100%;
  height: 120px;
  margin: 0;
  background-color: #9D84B7;   
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 14px;
}

.container_footer{
  display: flex;
  width: 80%;
  margin: auto;
  padding-top: 20px;
  padding-bottom: 0px;
  justify-content: space-around;  
}

.copy{
  margin-left: 30px;
  color: white;
  text-align: center;
}

.red img{
  float: left;
  width: 20px;
}

.red h4{
  float: left;
  color: white;
  margin-top: 3px;
  padding-left: 10px;
  cursor: pointer;
}

ul {
  display: flex;
  list-style-type: none;
  width: 80%;
  margin: auto;
  margin-top: 30px;
  margin-bottom: 30px;
  justify-content: space-around;
  background-color:  #091353;
  padding: 15px;
  border-radius: 7px;

}

li a{
  text-decoration: none;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: white;
  font-size: 18px;
}

li a:hover {
  color: #B2F9FC;
  font-weight: 600;
}

</style>