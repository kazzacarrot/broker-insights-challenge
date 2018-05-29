import { Component, OnInit } from '@angular/core';
import { POLICIES } from '../mock-policies';

@Component({
  selector: 'app-policies',
  templateUrl: './policies.component.html',
  styleUrls: ['./policies.component.css']
})
export class PoliciesComponent implements OnInit {
  policies = POLICIES;
  constructor() { }

  ngOnInit() {
  }

}
