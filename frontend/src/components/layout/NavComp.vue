<template>
    <Navbar>
        <template #logo>
            Consultant Control
        </template>
        <template #right-side>
            <div v-if="userDataIsEmpty()" class="buttons">
                <router-link to="/sign-up" class="button is-succes"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
            </div>

            <div v-else>
                <dropdown placement="bottom" :text="store.state.userData.email">
                    <list-group>
                        <list-group-item>
                            <template #prefix>
                                <svg class="w-4 h-4" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path></svg>
                            </template>
                            Profile
                        </list-group-item>
                        <list-group-item>
                            <template #prefix>
                                <svg class="w-4 h-4" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z"></path></svg>
                            </template>
                            Settings
                        </list-group-item>
                        <list-group-item>
                            <template #prefix>
                                <svg class="w-4 h-4" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z" clip-rule="evenodd"></path></svg>
                            </template>
                            Sign Out
                        </list-group-item>
                    </list-group>
                </dropdown>
            </div>
        </template>
    </Navbar>
</template>

<script setup>
    import { Navbar, Dropdown, ListGroup, ListGroupItem } from 'flowbite-vue'

    import { useStore } from 'vuex'

    const store = useStore()

    // this function aids with the reactivity of using the store
    function userDataIsEmpty() {
        if (Object.keys(store.state.userData).length == 0) {
            return true
        }
        
        return false
    }
</script>