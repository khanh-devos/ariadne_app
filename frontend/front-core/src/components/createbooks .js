import React from 'react'
import axios from "axios";
import { useForm } from 'react-hook-form';


const API = "http://127.0.0.1:8000/graphql/" 

function mutateNewBook(data){
  const body = {
    query: `mutation {
        create_book {
          title: ${data.title}
          published_at: ${data.published_at}
        }
    }`
}
  return axios.post(API, body).then((response) => {
    console.log(response.data.data)
    return response.data.data})
}


function Createbooks () {
  const {register, handleSubmit} = useForm({
    defaultValues:{
      title: "React 1",
      published_at: "2022-09-05"
    }
  })

  const submit = (data)=>{
    console.log(data);
    mutateNewBook(data);

  }
   

return (<>
  <h3>new book</h3>
  <form onSubmit={handleSubmit(submit)} >
    <label>title</label>
    <input type="text" value="React 1" />

    <label>published_at:</label>
    <input type="text" value="2022-09-05" />

    <br /><br />
    <input type="submit" />

  </form></>
  )
}

export default Createbooks 