import { Component, OnInit } from '@angular/core';
import { FbtService } from '../fbt.service';
import { Profile } from '../profile';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { MatDialog } from '@angular/material';
import { ProjectSelectorComponent } from '../project-selector/project-selector.component';

@Component({
  selector: 'app-profile-setup',
  templateUrl: './profile-setup.component.html',
  styleUrls: ['./profile-setup.component.css']
})
export class ProfileSetupComponent implements OnInit {

  profile: Profile = new Profile()
  target: any;
  source: any;

  constructor(
    private service: FbtService,
    private route: ActivatedRoute,
    private router: Router,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    if (id && id != 'new') {
      this.service.readProfile(id).subscribe(profile => {
        this.profile = profile;
      })
    }
  }

  /**
   * CHECKS IF ONE ELEMENT LIES BEFORE THE OTHER
   */
  isbefore(a, b) {
    if (a.parentNode == b.parentNode) {
      for (var cur = a; cur; cur = cur.previousSibling) {
        if (cur === b) {
          return true;
        }
      }
    }
    return false;
  }
  /**
   * LIST ITEM DRAP ENTERED
   */
  dragenter($event) {
    let target = $event.currentTarget;
    let sourceIndex = this.source.attributes['data-index'];
    let targetIndex = target.attributes['data-index'];
    if (this.isbefore(this.source, target)) {
      target.parentNode.insertBefore(this.source, target); // insert before
    }
    else {
      target.parentNode.insertBefore(this.source, target.nextSibling); //insert after
    }
    if (sourceIndex != targetIndex) {
      this.target = target;
    }
  }

  /**
   * LIST ITEM DRAG STARTED
   */
  dragstart($event) {
    this.source = $event.currentTarget;
    $event.dataTransfer.effectAllowed = 'move';
  }

  dragend($event) {
    let targetIndex = this.target.attributes['data-index'].value;
    let sourceIndex = this.source.attributes['data-index'].value;
    let project = this.profile.projects[sourceIndex];
    this.profile.projects.splice(sourceIndex, 1);
    this.profile.projects.splice(targetIndex, 0, project);    
  }

  save() {
    if (this.profile._id) {
      this.service.updateProfile(this.profile._id, this.profile).subscribe();
    } else {
      this.service.createProfile(this.profile).subscribe(profile => {
        this.router.navigate(['/profile/' + profile._id]);
      });
    }
  }

  openDialog(): void {
    let dialogRef = this.dialog.open(ProjectSelectorComponent, {
      width: '800px',
      data: { selected: this.profile.projects }
    });

    dialogRef.afterClosed().subscribe(mappings => {
      if (mappings) {
        mappings.forEach(mapping => {
          this.profile.projects.push(mapping);
        });
      }
    });
  }

  up(index: number) {
    if (index == 0) return;
    let project = this.profile.projects[index];
    this.profile.projects.splice(index, 1);
    this.profile.projects.splice(index - 1, 0, project);
  }

  down(index: number) {
    if (index > this.profile.projects.length - 1) return;
    let project = this.profile.projects[index];
    this.profile.projects.splice(index, 1);
    this.profile.projects.splice(index + 1, 0, project);
  }

  delete(index: number) {
    this.profile.projects.splice(index, 1);
  }

  run(): void {
    this.service.run(this.profile).subscribe();
    this.router.navigate(['/profile/' + this.profile._id + '/status']);
  }

}
