import React from 'react'
import axios from "axios";
import { useForm } from 'react-hook-form';
import cover from "../static/images/addimage.jpeg";

export const Input = ({ Label, Style, Type, ID, Accept, register, required }) =>{ 
  
  return (<div>
    <label>{Label} : </label> 
    
    { Type!=='checkbox' ? (Type!=="file" ? <br/> : '' ): '' }

    <input type={Type} id={ID} style={Style} {...register(Label, { required } )} 
           accept={Accept}
    />
    
  </div>
)}

const API = "http://127.0.0.1:8000/graphql/" 

function mutateNewBook(data){
  var image = document.getElementById("avatar-ID2");
  console.log(image.files[0]);

  let formData = new FormData();
    
  const config = {
    headers:{
      'Content-Type': 'multipart/form-data'
    }
  };

  formData.append("operations", `{
      "query": "mutation 
        { create_book(
            title: "${data.title}", 
            published_at: "${data.published_at}", 
            cover: "${image.files[0]}"
            ){ 
              title 
            }
        }"
    }`
  );




  const body = {
    query: `mutation {
        create_book (
          title: "${data.title}",
          published_at: "${data.published_at}",
          cover: "${image.files[0]}"
        )
        {
          title
        }
    }`
}
  return axios.post(API, formData, config).then((response) => {
    // console.log("response.data.data")
    console.log(response.data.data)

    if (response.data.data) {
      return response.data.data  
    } 
    else {
      let note = document.getElementById("Error-ID");
      note.textContent = "book created failed !".toUpperCase();
      setTimeout(()=>{
        note.textContent = null;
      }, 4000);

    }
  })
    
}


function Createbooks () {
  const {register, handleSubmit} = useForm({
    defaultValues:{
      title: "React 6",
      published_at: "2022-09-05"
    }
  })

  const submit = (data)=>{
    // console.log("data");
    // console.log(data);
    mutateNewBook(data);

  }
  
  
  const ClickImage=()=>{
    const input = document.getElementById("avatar-ID2");
    const show = document.getElementById("show-avatar-ID2");
    
    input.click();

    input.onchange = function(){
      const fr = new FileReader();
      const file = input.files[0];

      fr.readAsDataURL(file);

      fr.onload = ()=> { 
        show.src = fr.result 
      };

    }
  }

return (<>
  <h3>new book</h3>
  <p id={'Error-ID'} style={{color: "red"}}></p>
  <form onSubmit={handleSubmit(submit)} >
    
    <Input Label="title" Type="text" register={register}  />

    <Input Label="published_at" Type="text" register={register}  />



    <Input Label="add cover" Type="file" register={register} 
             ID="avatar-ID2"
             Accept="image/png, image/jpeg"
             
             Style={{display:"none"}}
    />

    <img src={cover} width={"10%"} height={"10%"}
            id="show-avatar-ID2" 
            onClick={ClickImage}
            
    />

    <br /><br />
    <input type="submit" />

  </form></>
  )
}

export default Createbooks 