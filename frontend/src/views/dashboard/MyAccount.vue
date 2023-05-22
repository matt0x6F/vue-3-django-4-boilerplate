<template>  
    <div class="columns is-multiline">
        <div class="column is-12">
            <h1 class="title">My Account</h1>
        </div>

        <div class="column is-12">
            <button @click="logout()" class="button is-danger">Log out</button>
        </div>
    </div>         
</template>

<script setup>
    import axios from 'axios';
    import { useStore } from 'vuex';
    import { useRouter } from 'vue-router';

    const store = useStore();
    const router = useRouter();

    async function getUserData() {
        store.commit('setIsLoading', true)

        const userData = await axios
        .get('/api/v1/users/me/')
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(JSON.stringify(error))
            return {}
        })

        store.commit('setUserData', userData)
        store.commit('setIsLoading', false)
    }
    
    async function logout() {
        await axios
            .post('/api/v1/token/logout/')
            .then(() => {
                console.log('Logged user out')
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })

        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        store.commit('removeToken')
        store.commit('resetUserData')

        router.push('/')
    }

    getUserData()
</script>