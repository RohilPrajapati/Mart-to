import { Product } from './index'
// import httpClient from '../../../plugins/axios'
import { createClient } from '../../../../plugins/axios'

export function fetchProduct(params = {}){
  return createClient().get(`${Product}/`,{params})
}

export function createProduct(post) {
    return createClient().post(`${Product}/`, post)
}

export function getProduct(id) {
  return createClient().get(`${Product}/${id}`,)
}
export function updateProduct(id,post) {
  return createClient().put(`${Product}/${id}`, post)
}

export function updateStatusProduct(id) {
  return createClient().patch(`${Product}/${id}`)
}