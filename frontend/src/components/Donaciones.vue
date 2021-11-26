  <template>
      
      <div class="container">
        <h1>Donaciones</h1>
         <img class="targetmision" src="https://i.postimg.cc/mg7xh0dC/nissan-dona-alimentos-1024x1024.jpg" alt="Compatitas misión">
        <div class="donaciones">
            <p class="donaciones-principal">Con su aporte, nuestros amigos peludos podrán recibir alimento, atención veterinaria y un refugio temporal, mientras consiguen un nuevo hogar.
            Puedes realizar tus aportes en dinero o en especie (alimento, medicina, insumos, etc) siguiendo las instrucciones a continuación.
            </p>
            <p><b> Donaciones de Dinero:</b></p>
            <p>Consignando a través de nuestra cuenta de ahorros en Bancolombia : 123-456789-10</p>
            <p>o por medio de transferencia Nequi : 3001234567</p>

           
            <p><b> Donaciones en especie: </b></p>
            <p>Nos encontramos ubicados en la Cra 1 # 2-3 del Barrio Primero de la Ciudad de Bogotá</p>


        </div>
       
</div>
</template>

<script> 

    export default {

        name:"Donaciones",
        
    }

</script>

<style>
.targetmision{
    width: 40%;
    float: left;
}
.donaciones{
    width: 60%;
    display: flex;
    text-align: left;
    flex-direction: column;
}
.donaciones-principal{
     line-height: 30px !important;
}
.donaciones p{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #606060;
        width: 100%;
        line-height: 10px;


}
h1{
    width: 100%;
    color: #9D84B7;
    
}
.targetmision{
    display: flex;
    width: 30%;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    flex-direction: column;
    -webkit-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
-moz-box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
box-shadow: 9px 10px 28px -17px rgba(0,0,0,0.75);
position: relative;


}
.targetmision img{
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

    

</style>