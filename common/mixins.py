class SerializerClassMixin:
    version_map = None

    def _get_serializer_class(self, version):
        return self.version_map[version]

    def get_serializer_class(self):
        if not self.version_map:
            raise Exception('Version Map not provided')

        version = self.request.version
        return self._get_serializer_class(version)
