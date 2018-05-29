import { Component } from '@angular/core';
import { Component, OnInit, Input } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  // policies = [{"customer_name": "Jeeves"}];
  policies:any;

  constructor(
    private http: HttpClient,
    ) { }

  ngOnInit() {
    this.policies = this.getPolicies()
    console.log(this.policies)
  }
  getPolicies(){
  return this.http.get<any[]>("http://localhost:8000/api/policy/").pipe(
      map(res => {
      return res.json().results.map(item=>new Policy(
        item.id,
        item.customer.name,
        item.customer.address,
        item.premium,
        item.insurer_name,
        item.policy_type,
      )
      })
    );
  }
}
