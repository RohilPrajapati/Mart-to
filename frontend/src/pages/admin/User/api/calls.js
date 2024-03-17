import { User } from './index'
import { createClient } from '../../../../plugins/axios'

export function getAllUser(params = {}) {
    return createClient().get(`${User}/`,{params})
}
export function updateStatusUser(id) {
    return createClient().put(`${User}/${id}/`)
}
// export function getPayment(id) {
//     return createClient().post(`${Order}/${id}`)
// }

