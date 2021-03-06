import { Component, OnInit, Inject } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { FbtService } from '../fbt.service';
import { Project } from '../project';
import { ProjectInstanceMapping } from '../project-instance-mapping';

@Component({
  selector: 'app-project-selector',
  templateUrl: './project-selector.component.html',
  styleUrls: ['./project-selector.component.css']
})
export class ProjectSelectorComponent implements OnInit {

  projects: Project[];
  projectInstanceMappings: ProjectInstanceMapping[] = [];

  constructor(
    public dialogRef: MatDialogRef<ProjectSelectorComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private service: FbtService
  ) {
    this.data.mappings = [];
  }

  cancel(): void {
    this.dialogRef.close();
  }

  add(projectInstanceMapping): void {
    let index = this.data.mappings.indexOf(projectInstanceMapping);
    if (index == -1) {
      this.data.mappings.push(projectInstanceMapping);
    }
  }

  ngOnInit() {
    this.service.readProjects().subscribe((projects: Project[]) => {
      projects.forEach(project => {
        let projectInstanceMapping = new ProjectInstanceMapping();
        projectInstanceMapping.project = project;
        projectInstanceMapping.instance = project.instances[0];
        this.projectInstanceMappings.push(projectInstanceMapping);
      });
    });
  }

  addAll() {
    this.projectInstanceMappings.forEach(mapping => {
      this.data.mappings.push(mapping);
    });
  }

  isSelected(id: string): boolean {
    if (!this.data.selected) {
      return false;
    }
    return this.data.selected.indexOf(id) != -1;
  }

}
