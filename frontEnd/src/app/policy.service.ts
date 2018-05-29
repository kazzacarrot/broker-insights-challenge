import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Policy } from './policy';
import { POLICIES } from './mock-policies';

@Injectable({
  providedIn: 'root'
})
export class PolicyService {

  constructor() { }

  getPolicies(): Observable<Policy[]>{
    return of(POLICIES);
  }
}
