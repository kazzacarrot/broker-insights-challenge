import { Component, OnInit } from '@angular/core';
import { PolicyService } from '../policy.service';
import { Policy } from '../policy';

@Component({
  selector: 'app-policies',
  templateUrl: './policies.component.html',
  styleUrls: ['./policies.component.css']
})
export class PoliciesComponent implements OnInit {
  policies: Policy[];
  constructor(private policyService: PolicyService) { }

  ngOnInit() {
    this.getPolicies();
  }

  getPolicies():void {
    this.policyService.getPolicies()
      .subscribe(policies => this.policies = policies);
  }

}
