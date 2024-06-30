// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: onos/config/v3/object.proto

package v3

import (
	fmt "fmt"
	_ "github.com/gogo/protobuf/gogoproto"
	proto "github.com/gogo/protobuf/proto"
	_ "github.com/gogo/protobuf/types"
	github_com_gogo_protobuf_types "github.com/gogo/protobuf/types"
	io "io"
	math "math"
	math_bits "math/bits"
	time "time"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf
var _ = time.Kitchen

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

type ObjectMeta struct {
	Key      string     `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	Version  uint64     `protobuf:"varint,2,opt,name=version,proto3" json:"version,omitempty"`
	Revision Revision   `protobuf:"varint,3,opt,name=revision,proto3,casttype=Revision" json:"revision,omitempty"`
	Created  time.Time  `protobuf:"bytes,4,opt,name=created,proto3,stdtime" json:"created"`
	Updated  time.Time  `protobuf:"bytes,5,opt,name=updated,proto3,stdtime" json:"updated"`
	Deleted  *time.Time `protobuf:"bytes,6,opt,name=deleted,proto3,stdtime" json:"deleted,omitempty"`
}

func (m *ObjectMeta) Reset()         { *m = ObjectMeta{} }
func (m *ObjectMeta) String() string { return proto.CompactTextString(m) }
func (*ObjectMeta) ProtoMessage()    {}
func (*ObjectMeta) Descriptor() ([]byte, []int) {
	return fileDescriptor_b78568cfc6f29733, []int{0}
}
func (m *ObjectMeta) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *ObjectMeta) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_ObjectMeta.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *ObjectMeta) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ObjectMeta.Merge(m, src)
}
func (m *ObjectMeta) XXX_Size() int {
	return m.Size()
}
func (m *ObjectMeta) XXX_DiscardUnknown() {
	xxx_messageInfo_ObjectMeta.DiscardUnknown(m)
}

var xxx_messageInfo_ObjectMeta proto.InternalMessageInfo

func (m *ObjectMeta) GetKey() string {
	if m != nil {
		return m.Key
	}
	return ""
}

func (m *ObjectMeta) GetVersion() uint64 {
	if m != nil {
		return m.Version
	}
	return 0
}

func (m *ObjectMeta) GetRevision() Revision {
	if m != nil {
		return m.Revision
	}
	return 0
}

func (m *ObjectMeta) GetCreated() time.Time {
	if m != nil {
		return m.Created
	}
	return time.Time{}
}

func (m *ObjectMeta) GetUpdated() time.Time {
	if m != nil {
		return m.Updated
	}
	return time.Time{}
}

func (m *ObjectMeta) GetDeleted() *time.Time {
	if m != nil {
		return m.Deleted
	}
	return nil
}

type Target struct {
	ID      TargetID      `protobuf:"bytes,1,opt,name=id,proto3,casttype=TargetID" json:"id,omitempty"`
	Type    TargetType    `protobuf:"bytes,2,opt,name=type,proto3,casttype=TargetType" json:"type,omitempty"`
	Version TargetVersion `protobuf:"bytes,3,opt,name=version,proto3,casttype=TargetVersion" json:"version,omitempty"`
}

func (m *Target) Reset()         { *m = Target{} }
func (m *Target) String() string { return proto.CompactTextString(m) }
func (*Target) ProtoMessage()    {}
func (*Target) Descriptor() ([]byte, []int) {
	return fileDescriptor_b78568cfc6f29733, []int{1}
}
func (m *Target) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *Target) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_Target.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *Target) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Target.Merge(m, src)
}
func (m *Target) XXX_Size() int {
	return m.Size()
}
func (m *Target) XXX_DiscardUnknown() {
	xxx_messageInfo_Target.DiscardUnknown(m)
}

var xxx_messageInfo_Target proto.InternalMessageInfo

func (m *Target) GetID() TargetID {
	if m != nil {
		return m.ID
	}
	return ""
}

func (m *Target) GetType() TargetType {
	if m != nil {
		return m.Type
	}
	return ""
}

func (m *Target) GetVersion() TargetVersion {
	if m != nil {
		return m.Version
	}
	return ""
}

func init() {
	proto.RegisterType((*ObjectMeta)(nil), "onos.config.v3.ObjectMeta")
	proto.RegisterType((*Target)(nil), "onos.config.v3.Target")
}

func init() { proto.RegisterFile("onos/config/v3/object.proto", fileDescriptor_b78568cfc6f29733) }

var fileDescriptor_b78568cfc6f29733 = []byte{
	// 352 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x90, 0xbf, 0x6a, 0xeb, 0x30,
	0x1c, 0x85, 0x2d, 0xc7, 0x37, 0x7f, 0x74, 0xef, 0x0d, 0xad, 0xe8, 0x60, 0x52, 0xb0, 0x82, 0x27,
	0x43, 0xc1, 0x86, 0x66, 0xeb, 0xd0, 0xc1, 0x64, 0xc9, 0x50, 0x0a, 0x22, 0x74, 0x77, 0xe2, 0x5f,
	0x8c, 0xdb, 0x24, 0x32, 0x8e, 0x62, 0xc8, 0xd0, 0x77, 0xc8, 0x13, 0xf4, 0x79, 0x32, 0x66, 0xec,
	0xe4, 0x16, 0xe7, 0x2d, 0x32, 0x15, 0x49, 0x71, 0x3a, 0x96, 0x6e, 0x92, 0xbf, 0xf3, 0x99, 0xa3,
	0x83, 0xaf, 0xf9, 0x92, 0xaf, 0x82, 0x29, 0x5f, 0xce, 0xd2, 0x24, 0x28, 0x06, 0x01, 0x9f, 0x3c,
	0xc3, 0x54, 0xf8, 0x59, 0xce, 0x05, 0x27, 0x5d, 0x09, 0x7d, 0x0d, 0xfd, 0x62, 0xd0, 0xbb, 0x4a,
	0x78, 0xc2, 0x15, 0x0a, 0xe4, 0x49, 0xa7, 0x7a, 0x34, 0xe1, 0x3c, 0x99, 0x43, 0xa0, 0x6e, 0x93,
	0xf5, 0x2c, 0x10, 0xe9, 0x02, 0x56, 0x22, 0x5a, 0x64, 0x3a, 0xe0, 0xbe, 0x99, 0x18, 0x3f, 0xaa,
	0xff, 0x3e, 0x80, 0x88, 0xc8, 0x05, 0x6e, 0xbc, 0xc0, 0xc6, 0x46, 0x7d, 0xe4, 0x75, 0x98, 0x3c,
	0x12, 0x1b, 0xb7, 0x0a, 0xc8, 0x57, 0x29, 0x5f, 0xda, 0x66, 0x1f, 0x79, 0x16, 0xab, 0xaf, 0xc4,
	0xc3, 0xed, 0x1c, 0x8a, 0x54, 0xa1, 0x86, 0x44, 0xe1, 0xbf, 0x63, 0x49, 0xdb, 0xec, 0xf4, 0x8d,
	0x9d, 0x29, 0xb9, 0xc7, 0xad, 0x69, 0x0e, 0x91, 0x80, 0xd8, 0xb6, 0xfa, 0xc8, 0xfb, 0x7b, 0xdb,
	0xf3, 0x75, 0x2f, 0xbf, 0xee, 0xe5, 0x8f, 0xeb, 0x5e, 0x61, 0x7b, 0x57, 0x52, 0x63, 0xfb, 0x41,
	0x11, 0xab, 0x25, 0xe9, 0xaf, 0xb3, 0x58, 0xf9, 0x7f, 0x7e, 0xe3, 0x9f, 0x24, 0x72, 0x87, 0x5b,
	0x31, 0xcc, 0x41, 0xfa, 0xcd, 0x1f, 0x7d, 0x4b, 0xbb, 0x27, 0xc1, 0x7d, 0xc5, 0xcd, 0x71, 0x94,
	0x27, 0x20, 0x88, 0x8b, 0xcd, 0x34, 0xd6, 0xd3, 0x84, 0xa4, 0x2a, 0xa9, 0x39, 0x1a, 0xca, 0xf7,
	0x6a, 0x3a, 0x1a, 0x32, 0x33, 0x8d, 0x89, 0x8b, 0x2d, 0xb1, 0xc9, 0x40, 0x4d, 0xd5, 0x09, 0xbb,
	0xc7, 0x92, 0x62, 0xcd, 0xc7, 0x9b, 0x0c, 0x98, 0x62, 0xe4, 0xe6, 0x7b, 0xd1, 0x86, 0x8a, 0x5d,
	0x1e, 0x4b, 0xfa, 0x5f, 0xc7, 0x9e, 0x34, 0x38, 0x8f, 0x1c, 0xda, 0xbb, 0xca, 0x41, 0xfb, 0xca,
	0x41, 0x9f, 0x95, 0x83, 0xb6, 0x07, 0xc7, 0xd8, 0x1f, 0x1c, 0xe3, 0xfd, 0xe0, 0x18, 0x93, 0xa6,
	0xea, 0x3e, 0xf8, 0x0a, 0x00, 0x00, 0xff, 0xff, 0xde, 0x9f, 0x0f, 0x4b, 0x26, 0x02, 0x00, 0x00,
}

func (m *ObjectMeta) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *ObjectMeta) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *ObjectMeta) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.Deleted != nil {
		n1, err1 := github_com_gogo_protobuf_types.StdTimeMarshalTo(*m.Deleted, dAtA[i-github_com_gogo_protobuf_types.SizeOfStdTime(*m.Deleted):])
		if err1 != nil {
			return 0, err1
		}
		i -= n1
		i = encodeVarintObject(dAtA, i, uint64(n1))
		i--
		dAtA[i] = 0x32
	}
	n2, err2 := github_com_gogo_protobuf_types.StdTimeMarshalTo(m.Updated, dAtA[i-github_com_gogo_protobuf_types.SizeOfStdTime(m.Updated):])
	if err2 != nil {
		return 0, err2
	}
	i -= n2
	i = encodeVarintObject(dAtA, i, uint64(n2))
	i--
	dAtA[i] = 0x2a
	n3, err3 := github_com_gogo_protobuf_types.StdTimeMarshalTo(m.Created, dAtA[i-github_com_gogo_protobuf_types.SizeOfStdTime(m.Created):])
	if err3 != nil {
		return 0, err3
	}
	i -= n3
	i = encodeVarintObject(dAtA, i, uint64(n3))
	i--
	dAtA[i] = 0x22
	if m.Revision != 0 {
		i = encodeVarintObject(dAtA, i, uint64(m.Revision))
		i--
		dAtA[i] = 0x18
	}
	if m.Version != 0 {
		i = encodeVarintObject(dAtA, i, uint64(m.Version))
		i--
		dAtA[i] = 0x10
	}
	if len(m.Key) > 0 {
		i -= len(m.Key)
		copy(dAtA[i:], m.Key)
		i = encodeVarintObject(dAtA, i, uint64(len(m.Key)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *Target) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *Target) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *Target) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if len(m.Version) > 0 {
		i -= len(m.Version)
		copy(dAtA[i:], m.Version)
		i = encodeVarintObject(dAtA, i, uint64(len(m.Version)))
		i--
		dAtA[i] = 0x1a
	}
	if len(m.Type) > 0 {
		i -= len(m.Type)
		copy(dAtA[i:], m.Type)
		i = encodeVarintObject(dAtA, i, uint64(len(m.Type)))
		i--
		dAtA[i] = 0x12
	}
	if len(m.ID) > 0 {
		i -= len(m.ID)
		copy(dAtA[i:], m.ID)
		i = encodeVarintObject(dAtA, i, uint64(len(m.ID)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func encodeVarintObject(dAtA []byte, offset int, v uint64) int {
	offset -= sovObject(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *ObjectMeta) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.Key)
	if l > 0 {
		n += 1 + l + sovObject(uint64(l))
	}
	if m.Version != 0 {
		n += 1 + sovObject(uint64(m.Version))
	}
	if m.Revision != 0 {
		n += 1 + sovObject(uint64(m.Revision))
	}
	l = github_com_gogo_protobuf_types.SizeOfStdTime(m.Created)
	n += 1 + l + sovObject(uint64(l))
	l = github_com_gogo_protobuf_types.SizeOfStdTime(m.Updated)
	n += 1 + l + sovObject(uint64(l))
	if m.Deleted != nil {
		l = github_com_gogo_protobuf_types.SizeOfStdTime(*m.Deleted)
		n += 1 + l + sovObject(uint64(l))
	}
	return n
}

func (m *Target) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.ID)
	if l > 0 {
		n += 1 + l + sovObject(uint64(l))
	}
	l = len(m.Type)
	if l > 0 {
		n += 1 + l + sovObject(uint64(l))
	}
	l = len(m.Version)
	if l > 0 {
		n += 1 + l + sovObject(uint64(l))
	}
	return n
}

func sovObject(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozObject(x uint64) (n int) {
	return sovObject(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *ObjectMeta) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowObject
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: ObjectMeta: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: ObjectMeta: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Key", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Key = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 2:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field Version", wireType)
			}
			m.Version = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.Version |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		case 3:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field Revision", wireType)
			}
			m.Revision = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.Revision |= Revision(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		case 4:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Created", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if err := github_com_gogo_protobuf_types.StdTimeUnmarshal(&m.Created, dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 5:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Updated", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if err := github_com_gogo_protobuf_types.StdTimeUnmarshal(&m.Updated, dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 6:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Deleted", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.Deleted == nil {
				m.Deleted = new(time.Time)
			}
			if err := github_com_gogo_protobuf_types.StdTimeUnmarshal(m.Deleted, dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipObject(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if (skippy < 0) || (iNdEx+skippy) < 0 {
				return ErrInvalidLengthObject
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *Target) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowObject
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: Target: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: Target: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field ID", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.ID = TargetID(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Type", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Type = TargetType(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 3:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Version", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowObject
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthObject
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthObject
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.Version = TargetVersion(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipObject(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if (skippy < 0) || (iNdEx+skippy) < 0 {
				return ErrInvalidLengthObject
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipObject(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	depth := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowObject
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowObject
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
		case 1:
			iNdEx += 8
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowObject
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthObject
			}
			iNdEx += length
		case 3:
			depth++
		case 4:
			if depth == 0 {
				return 0, ErrUnexpectedEndOfGroupObject
			}
			depth--
		case 5:
			iNdEx += 4
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
		if iNdEx < 0 {
			return 0, ErrInvalidLengthObject
		}
		if depth == 0 {
			return iNdEx, nil
		}
	}
	return 0, io.ErrUnexpectedEOF
}

var (
	ErrInvalidLengthObject        = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowObject          = fmt.Errorf("proto: integer overflow")
	ErrUnexpectedEndOfGroupObject = fmt.Errorf("proto: unexpected end of group")
)