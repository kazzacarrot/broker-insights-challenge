import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Policy } from './policy';
import { POLICIES } from './mock-policies';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { pluck, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PolicyService {
  private policiesURL = "http://localhost:8000/api/policy/";

  constructor(
    private http: HttpClient
  ) { }

  getPolicies(): Observable<Policy[]>{
    return this.http.get<Policy[]>(this.policiesURL).pipe(
        pluck("objects"),
        map(function(policies){
            var reformattedArray = policies.map(obj =>{ 
               var rObj = {};
               rObj.customer_name = obj.customer.name;
               rObj.customer_address = obj.customer.address;
               rObj.insurer = obj.insurer.name;
               rObj.premium = obj.premium;
               rObj.policy_type = obj.policy_type;
               return rObj;
            })
            return reformattedArray;
        }), 
        
    )
  }
}
