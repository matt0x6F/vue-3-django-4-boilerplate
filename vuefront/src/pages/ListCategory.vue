<template>
    <h1>Listado</h1>
</template>
<script>
export default {
    mounted(){
        this.$axios.get("http://localhost:8000/api/products/?format=json").then((res)=>{
            console.log(res)
        })
    }
}
</script>