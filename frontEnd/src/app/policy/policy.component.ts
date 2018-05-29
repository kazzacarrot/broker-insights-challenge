import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-policy',
  templateUrl: './policy.component.html',
  styleUrls: ['./policy.component.css']
})
export class PolicyComponent implements OnInit {
  @Input() policy_obj;
  expanded:boolean = false;

  constructor() { }

  ngOnInit() {
  }
  
  toggleExpand(){
    this.expanded = !this.expanded;
  }
}
