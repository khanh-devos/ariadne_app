import React from 'react'
import axios from "axios";
import { useForm } from 'react-hook-form';


export const Input = ({ Label, Style, Type, ID, register, required }) =>{ 
  
  return (<div>
    <label>{Label} : </label> 
    
    { Type!=='checkbox' ? (Type!=="file" ? '' : '' ): '' }

    <input type={Type} id={ID} style={Style} {...register(Label, { required } )} 
           className="input-class-0"
    />
    
  </div>
)}

const API = "http://127.0.0.1:8000/graphql/" 

function mutateNewBook(data){
  const body = {
    query: ` mutation {
        create_book (
          title: "${data.title}",
          published_at: "${data.published_at}"
        )
        {
          title
        }
    }`
}
  return axios.post(API, body).then((response) => {
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
      title: "React 1",
      published_at: "2022-09-05"
    }
  })

  const submit = (data)=>{
    // console.log("data");
    // console.log(data);
    mutateNewBook(data);

  }
   

return (<>
  <h3>new book</h3>
  <p id={'Error-ID'} style={{color: "red"}}></p>
  <form onSubmit={handleSubmit(submit)} >
    
    <Input Label="title" Type="text" register={register}  />

    <Input Label="published_at" Type="text" register={register}  />

    <br /><br />
    <input type="submit" />

  </form></>
  )
}

export default Createbooks 