   <template>
      
      <div class="container">
        <h1>Misión</h1>
         <img class="targetmision" src="https://i.postimg.cc/Y21h3VjH/MSION-Mesa-de-trabajo-1.jpg" alt="Compatitas misión">
        <div class="mision">
            <p >Buscamos ayudar a algunos de los cientos de mascotas que diariamente son 
                abandonadas en las calles de nuestras ciudades, para brindarles una segunda oportunidad.
            </p>
            <p >
    
                Somos un grupo de entusiastas, que busca a través de la tecnología, 
                aportar para mejorar las condiciones de vida de muchos animalitos, conectando sus historias con personas dispuestas a ayudar</p>


        </div>
       
</div>
</template>

<script>

export default {
    name: 'Mision',
}

</script>

<style>
.targetmision{
    width: 40%;
    float: left;
}
.mision{
    width: 60%;
    display: flex;
    align-items: center;
    flex-direction: column;
}
.mision p{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #606060;
        width: 100%;
        line-height: 30px;


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