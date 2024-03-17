<template>
        <div class="q-ma-sm">
            <h5>Product List</h5>
            <div class="row no-wrap q-my-lg">
                <q-input class="q-mr-sm" dense outlined rounded @keyup="getProduct()" v-model="search" placeholder="Search Product" />
                <q-btn rounded color="grey-3" text-color="grey-8" icon="search" unelevated />
                <q-btn class="q-mx-sm" color="primary" @click="$router.push('product/add'); " rounded label="Add New product" />
            </div>
            <q-markup-table :separator="separator" flat bordered class="">
                <thead>
                    <tr class="text-white bg-grey">
                        <th style="width: 220px;">Name</th>
                        <th style="width: 140px;">Image</th>
                        <th style="width: 140px;">Stock</th>
                        <th style="width: 370px;">Description</th>
                        <th style="width: 100px;">Price</th>
                        <th style="width: 100px;">status</th>
                        <th style="width: 220px;">action</th>
                    </tr>
                </thead>
                <tbody>
                    
                    <tr v-for="product in products" :key="product.id">
                        <td class="text-left">{{ product.name }}</td>
                        <td class="text-center"><q-img
                            :src="url_backend+product.image"
                            spinner-color="white"
                            style="height: 120px; max-width: 140px; min-width:120px"
                            contain
                            />
                            
                        </td>
                        <td class="text-center">{{product.stock}}</td>
                        <td class="text-left">{{product.description}}</td>
                        <td class="text-right">Rs. {{ product.price }}</td>
                        <td class="text-center" v-if="product.status">Enabled</td>
                        <td class="text-center" v-else>Disabled</td>
                        <td class="text-center">
                            <q-btn @click="$router.push({name:'adminproductedit',query: { id: product.id }})" class="q-mr-sm" color="secondary" label="Edit" />
                            <q-btn @click="updateStatus(product.id)" v-if="product.status" color="red-7" label="Disable" />
                            <q-btn @click="updateStatus(product.id)" v-else color="green-7" label="Enable" />
                        </td>
                    </tr>
                </tbody>
            </q-markup-table>
        </div>
</template>

<script>
import { fetchProduct,updateStatusProduct } from './api/calls'
import { API_HOST } from '../../../config/index'
import { Store } from '../../../store/index'
export default {
    name: 'AdminProduct',
    data(){
        return {
            search:"",
            products:{},
            separator: 'cell',
            url_backend:API_HOST,
            p_status:true,
            user: Store.state.user.user.admin
        }
    },
    created() {
        this.getProduct()
    },
    methods:{
        async getProduct(){
            console.log(this.user)
            const response = await fetchProduct({search:this.search}).then( data => {
                this.products = data.data.data;
                // console.log(this.product);
            })
        },
        async searchProduct(word){
            const response = await fetchProduct().then(data => {
                this.products.data.data.data;
            })
        },
        async updateStatus(id){
            await updateStatusProduct(id).then(data => {
                this.$q.notify({
                    color: "green-5",
                    textColor: "white",
                    icon: "info",
                    message: "Product status is updated"
                });
                this.getProduct()
            }).catch(error =>{
                this.$q.notify({
                    color: "red-5",
                    textColor: "white",
                    icon: "info",
                    message: "Product status is not updated"
                });
            })
        }
        // async fetchData(user_id){
    //   const response = await getProfile(user_id).then( data => {
    }
}
</script>