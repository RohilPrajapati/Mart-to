import { Product } from './index'
// import httpClient from '../../../plugins/axios'
import { createClient } from '../../../plugins/axios'

export function fetchProduct(params = {}) {
    return createClient().get(`${Product}/`, { params })
}
export function fetchProductDetail(id,params = {}) {
    console.log("working")
    return createClient().get(`${Product}/${id}`, { params })
}