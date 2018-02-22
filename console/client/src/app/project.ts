import { ProjectInstance } from './project-instance';
import { ProjectName } from './project-name';

export class Project {
  _id: string;
  name: ProjectName;
  instances: ProjectInstance[];
}
