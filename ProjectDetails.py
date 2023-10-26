# src/PAIEA/ProjectDetails.py

class ProjectDetails:
    def __init__(self):
        self.projects = {}

    def add_project(self, project_id, project_info):
        """
        Add a new project to the projects dictionary.
        :param project_id: Unique identifier for the project.
        :param project_info: Dictionary containing project details.
        """
        if project_id not in self.projects:
            self.projects[project_id] = project_info
        else:
            print(f"Project with id {project_id} already exists.")

    def update_project(self, project_id, updated_info):
        """
        Update an existing project's details.
        :param project_id: Unique identifier for the project.
        :param updated_info: Dictionary containing updated project details.
        """
        if project_id in self.projects:
            self.projects[project_id].update(updated_info)
        else:
            print(f"Project with id {project_id} does not exist.")

    def retrieve_project(self, project_id):
        """
        Retrieve details of a specific project.
        :param project_id: Unique identifier for the project.
        :return: Dictionary containing project details if project exists, else None.
        """
        if project_id in self.projects:
            return self.projects[project_id]
        else:
            print(f"Project with id {project_id} does not exist.")
            return None
