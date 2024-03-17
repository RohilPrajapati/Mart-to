import { Payment } from './index'
import { createClient } from '../../../plugins/axios'

export function addPaymentData(data) {
    return createClient().post(`${Payment}`, data)
}
// export function getPayment(id) {
//     return createClient().post(`${Order}/${id}`)
// }

