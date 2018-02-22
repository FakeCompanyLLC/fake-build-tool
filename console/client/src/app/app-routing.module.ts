import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { ProfileStatusComponent } from './profile-status/profile-status.component';
import { ProfileSetupComponent } from './profile-setup/profile-setup.component';
import { ProjectComponent } from './project/project.component';
import { ProjectSetupComponent } from './project-setup/project-setup.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProfileListComponent } from './profile-list/profile-list.component';

const routes: Routes = [
  { path: 'profile', component: ProfileComponent, children: [
    { path: '', component: ProfileListComponent },
    { path: ':id', component: ProfileSetupComponent },
    { path: ':id/status', component: ProfileStatusComponent }
  ] },
  { path: 'project', component: ProjectComponent, children: [
    { path: '', component: ProjectListComponent },
    { path: ':id', component: ProjectSetupComponent }
  ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
