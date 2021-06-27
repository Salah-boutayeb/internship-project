/*  */
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const demander=(params)=>{
  M.toast({html: "votre demande a été envoyer avec succée"})
    $.ajax({
        type: 'POST',
        url:`/stage/demande/`,
        data:{
          'csrfmiddlewaretoken':csrf[0].value,
          'id':params
      },
        success: (response)=>{
          console.log(response.data); 
          document.getElementById('demander'+params).classList.add('disabled')
          M.toast({html: response.data})
          },
        error: (error)=>{
            console.error(error);
        },
    })
}