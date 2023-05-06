<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>App Products</strong>
            </router-link>
            <div class="navbar-start">
                <div class="navbar-item">
                    <router-link to="/about" class="navbar-link">About</router-link>
                    <router-link to="/products" class="navbar-link">Products</router-link>
                </div>
            </div>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link to="/sign-up" class="button is-succes"><strong>Sign up</strong></router-link>
                        <router-link to="/log-in" class="button is-light">Log in</router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'NavComp'
    }
</script>