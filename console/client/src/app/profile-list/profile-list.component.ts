import { Component, OnInit } from '@angular/core';
import { FbtService } from '../fbt.service';
import { Profile } from '../profile';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile-list',
  templateUrl: './profile-list.component.html',
  styleUrls: ['./profile-list.component.css']
})
export class ProfileListComponent implements OnInit {

  profiles: Profile[];

  constructor(
    private service: FbtService,
    public dialog: MatDialog,
    private router: Router
  ) { }

  ngOnInit() {
    this.service.readProfiles().subscribe((profiles: Profile[]) => {
      this.profiles = profiles;
    });
  }

  copy(id): void {
    this.service.copyProfile(id).subscribe((profile: Profile) => {
      this.profiles.push(profile);
    });
  }

  add(): void {
    this.openDialog();
  }

  openDialog(): void {
    let dialogRef = this.dialog.open(ProfileAddComponent, {
      width: '500px'
    });

    dialogRef.afterClosed().subscribe(name => {
      if (name) {
        let profile = new Profile();
        profile.name = name;
        this.service.createProfile(profile).subscribe((profile: Profile) => {
          this.router.navigate(['/profile/' + profile._id]);
        });
      }
    });
  }

  run(id: string): void {
    this.service.readProfile(id).subscribe((profile: Profile) => {
      this.service.run(profile).subscribe();
      this.router.navigate(['/profile/' + profile._id + '/status']);
    });
  }

  remove(profile: Profile): void {
    this.service.deleteProfile(profile._id).subscribe(() => {
      this.profiles.splice(this.profiles.indexOf(profile), 1);
    });
  }

}

@Component({
  selector: 'app-profile-add',
  templateUrl: './profile-add.component.html',
  styleUrls: ['./profile-add.component.css']
})
export class ProfileAddComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ProfileAddComponent>
  ) { }

  cancel(): void {
    this.dialogRef.close();
  }

  ngOnInit() {

  }

}
