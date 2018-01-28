class Course(object):
    def __init__(self, id, name, prereqs = [], equivalences = []):
        """
        id: string containing the course's id
        name: string containing the course's name
        prereqs: list of strings containing the course's pre-requisite
        equivalences: list of strings containing the course's equivalences
        """
        super(Course, self).__init__()
        self._id = id
        self._name = name
        self._prereqs = prereqs
        self._equivalences = equivalences

    @property
    def id():
        return self._id

    @property
    def name():
        return self._name

    @property
    def prereqs():
        return self._prereqs

    @property
    def equivalences():
        return self._equivalences

    def displayData(self):
        str_id = "Código: {}".format(self._id)
        str_name = "Nome: {}".format(self._name)
        str_prereqs = "Pré-requesito(s): {}".format(self._prereqs)
        str_equivalences = "Equivalência(s): {}".format(self._equivalences)
        str_data = [str_id, str_name, str_prereqs, str_equivalences]
        return "\n".join([data for data in str_data])
